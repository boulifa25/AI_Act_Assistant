"""Agent LangGraph : route une demande vers la recherche dans le texte ou la classification du risque.

            ┌─> rechercher_texte ─┐
  routeur ──┤                     ├─> reponse_finale
            └─> classer_risque ───┘

Usage : python -m app.agent.graph "Un chatbot RH qui trie des CV" [--provider mistral]
"""
import json
import operator
from typing import Annotated, Literal, TypedDict

from langgraph.graph import END, START, StateGraph

from app.llm.base import LLMProvider, LLMResponse, get_provider
from app.rag.answer import SYSTEM_PROMPT, build_prompt, cited_labels
from app.rag.retriever import Result, search

Route = Literal["question", "classification"]
NIVEAUX = ["inacceptable", "haut risque", "risque limité", "risque minimal"]


class AgentState(TypedDict, total=False):
    input: str
    mode: Literal["auto", "question", "classification"]
    route: Route
    sources: list[Result]
    answer: str
    cited: list[str]
    classification: dict
    llm_calls: Annotated[list[LLMResponse], operator.add]  # cumul pour latence et coût


# --- Nœud routeur -----------------------------------------------------------------------

ROUTER_SYSTEM = """Tu tries des demandes adressées à un assistant sur le règlement européen sur l'IA (AI Act).
- CAS : la demande décrit un système ou un usage d'IA concret dont il faut déterminer le niveau de risque
  (ex. « Un chatbot RH qui trie des CV », « Mon appli de reconnaissance faciale est-elle autorisée ? »).
- QUESTION : toute autre question sur le contenu du texte (définitions, obligations, dates, sanctions...).
Réponds par un seul mot : CAS ou QUESTION."""


def routeur(state: AgentState, llm: LLMProvider) -> AgentState:
    if state.get("mode", "auto") != "auto":
        return {"route": state["mode"], "llm_calls": []}
    r = llm.generate(state["input"], system=ROUTER_SYSTEM)
    route: Route = "classification" if "CAS" in r.text.upper() else "question"
    return {"route": route, "llm_calls": [r]}


# --- Outil rechercher_texte -------------------------------------------------------------

def rechercher_texte(state: AgentState) -> AgentState:
    return {"sources": search(state["input"], k=5)}


# --- Outil classer_risque ---------------------------------------------------------------
# Trois vérifications courtes plutôt qu'un seul gros appel : un modèle 7B s'effondre quand on lui
# demande trois raisonnements à la fois sur ~5 000 tokens (3/7 cas réussis contre 7/7 en cloud).
# Chaque vérification ne voit que sa partie du texte, en entier, et on s'arrête au premier niveau atteint.

CHECKS = [  # (clé, niveau si applicable, partie du texte, question)
    ("article_5", "inacceptable", "5",
     "Ce système relève-t-il d'une des pratiques interdites énumérées à l'article 5, paragraphe 1 ?"),
    ("annexe_iii", "haut risque", "Annexe III",
     "Ce système relève-t-il d'un des domaines listés à l'annexe III ? Parcours tous les points 1 à 8 "
     "(biométrie, infrastructures critiques, éducation, emploi, services essentiels, répression, migration, justice)."),
    ("article_50", "risque limité", "50",
     "Ce système interagit-il directement avec des personnes physiques, ou génère-t-il des contenus de synthèse "
     "(texte, image, audio, vidéo), au sens de l'article 50 ?"),
]

CHECK_SYSTEM = """Tu vérifies un point précis du règlement (UE) 2024/1689 (AI Act), UNIQUEMENT à partir des extraits fournis.
Réponds uniquement en JSON :
{"applicable": true ou false, "point": "le point précis du texte qui s'applique, ou une chaîne vide", "justification": "1 à 2 phrases"}"""


def _applies(finding: dict) -> bool:
    """Tolère "true" en texte, que les petits modèles renvoient parfois."""
    value = finding.get("applicable")
    return value is True or str(value).strip().lower() in ("true", "oui")


def verifier(description: str, article: str, question: str, llm: LLMProvider):
    sources = search(description, k=10, articles=[article])  # la partie du texte en entier (5 à 8 chunks)
    prompt = build_prompt(f"{question}\nSystème à analyser : {description}", sources)
    r = llm.generate(prompt, system=CHECK_SYSTEM, json_mode=True)
    try:
        finding = json.loads(r.text)
    except json.JSONDecodeError:
        finding = {"applicable": False, "point": "", "justification": f"Réponse illisible : {r.text[:200]}"}
    return finding, sources, r


def classer_risque(state: AgentState, llm: LLMProvider) -> AgentState:
    """Le LLM constate, le code décide : niveau le plus élevé dont la vérification est positive."""
    verifications, sources, calls = {}, [], []
    niveau, justification, articles = "risque minimal", "", []
    for key, level, article, question in CHECKS:
        finding, found, r = verifier(state["input"], article, question, llm)
        verifications[key] = {"applicable": _applies(finding), "point": finding.get("point", "")}
        sources += found
        calls.append(r)
        if _applies(finding):
            niveau, justification = level, str(finding.get("justification", ""))
            articles = [found[0].label] if found else []
            break
    if niveau == "risque minimal":
        justification = ("Aucune pratique interdite (article 5), aucun domaine à haut risque (annexe III) "
                         "ni obligation de transparence (article 50) n'a été identifié dans le texte.")
    classification = {"niveau": niveau, "justification": justification.strip(),
                      "verifications": verifications, "articles": articles}
    return {"sources": sources, "classification": classification, "llm_calls": calls}


# --- Nœud réponse finale ----------------------------------------------------------------

def reponse_finale(state: AgentState, llm: LLMProvider) -> AgentState:
    if state["route"] == "classification":
        c = state["classification"]
        text = f"Niveau de risque : {c['niveau']}\n\n{c['justification']}\n\nSources : {', '.join(c['articles']) or 'aucune'}"
        return {"answer": text, "cited": c["articles"]}
    r = llm.generate(build_prompt(state["input"], state["sources"]), system=SYSTEM_PROMPT)
    return {"answer": r.text, "cited": cited_labels(r.text, state["sources"]), "llm_calls": [r]}


# --- Graphe -----------------------------------------------------------------------------

def build_graph(llm: LLMProvider):
    g = StateGraph(AgentState)
    g.add_node("routeur", lambda s: routeur(s, llm))
    g.add_node("rechercher_texte", rechercher_texte)
    g.add_node("classer_risque", lambda s: classer_risque(s, llm))
    g.add_node("reponse_finale", lambda s: reponse_finale(s, llm))

    g.add_edge(START, "routeur")
    g.add_conditional_edges("routeur", lambda s: s["route"],
                            {"question": "rechercher_texte", "classification": "classer_risque"})
    g.add_edge("rechercher_texte", "reponse_finale")
    g.add_edge("classer_risque", "reponse_finale")
    g.add_edge("reponse_finale", END)
    return g.compile()


def run(text: str, mode: str = "auto", provider: str | None = None) -> AgentState:
    return build_graph(get_provider(provider)).invoke({"input": text, "mode": mode, "llm_calls": []})


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    parser.add_argument("--mode", default="auto", choices=["auto", "question", "classification"])
    parser.add_argument("--provider", choices=["ollama", "mistral"])
    args = parser.parse_args()

    s = run(args.text, args.mode, args.provider)
    calls = s["llm_calls"]
    print(f"Route : {s['route']}\n")
    print(s["answer"])
    print(f"\n{len(calls)} appel(s) LLM | {sum(c.latency_s for c in calls):.1f} s | "
          f"{sum(c.cost_usd for c in calls):.6f} $")
