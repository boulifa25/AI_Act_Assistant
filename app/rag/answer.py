"""Chaîne RAG complète : question -> retriever -> prompt -> LLM -> réponse sourcée.

Usage : python -m app.rag.answer "Quelles pratiques sont interdites ?" [--provider mistral]
"""
import re
from dataclasses import dataclass, field

from app.llm.base import LLMProvider, LLMResponse, get_provider
from app.rag.retriever import Result, search

SYSTEM_PROMPT = """Tu es un assistant spécialisé dans le règlement (UE) 2024/1689 sur l'intelligence artificielle (AI Act).

Règles strictes :
1. Réponds UNIQUEMENT à partir des extraits fournis. N'utilise jamais tes connaissances générales.
2. Cite tes sources entre crochets, exactement comme elles sont étiquetées, par exemple [Article 5] ou [Annexe III].
3. Si les extraits ne contiennent pas l'information demandée, réponds exactement : « Je ne sais pas : les extraits fournis ne permettent pas de répondre à cette question. »
4. Réponds en français, de façon concise et précise."""

REFUSAL_MARKER = "je ne sais pas"


@dataclass
class Answer:
    question: str
    text: str
    sources: list[Result]
    llm: LLMResponse
    cited: list[str] = field(default_factory=list)

    @property
    def refused(self) -> bool:
        return REFUSAL_MARKER in self.text.lower()


def build_prompt(question: str, results: list[Result]) -> str:
    excerpts = "\n\n".join(
        f"[{r.label}]" + (f" {r.titre}" if r.titre else "") + f"\n{r.contenu}"
        for r in results
    )
    return f"Extraits du règlement :\n\n{excerpts}\n\n---\nQuestion : {question}"


def answer(question: str, provider: LLMProvider | None = None, k: int = 5) -> Answer:
    provider = provider or get_provider()
    results = search(question, k=k)
    llm = provider.generate(build_prompt(question, results), system=SYSTEM_PROMPT)
    return Answer(question, llm.text, results, llm, cited_labels(llm.text, results))


def cited_labels(text: str, results: list[Result]) -> list[str]:
    """Sources effectivement citées. Le modèle écrit parfois [Article 5(1)(a)] :
    on accepte un suffixe, mais pas un chiffre (Article 50) ni un numéral romain (Annexe III)."""
    labels = dict.fromkeys(r.label for r in results)
    return [l for l in labels if re.search(re.escape(l) + r"(?![\dIVXL])", text)]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    parser.add_argument("--provider", choices=["ollama", "mistral"])
    args = parser.parse_args()

    a = answer(args.question, get_provider(args.provider))
    print(a.text)
    print(f"\nSources récupérées : {', '.join(dict.fromkeys(r.label for r in a.sources))}")
    print(f"Articles cités     : {', '.join(a.cited) or 'aucun'}")
    print(f"{a.llm.model} | {a.llm.input_tokens}+{a.llm.output_tokens} tokens | "
          f"{a.llm.latency_s:.1f} s | {a.llm.cost_usd:.6f} $")
