"""Évaluation comparative des modèles sur eval/questions.jsonl -> eval/results.md

Usage :
  python -m eval.run_eval                       # les deux modèles
  python -m eval.run_eval --providers mistral   # un seul
  python -m eval.run_eval --report-only         # régénère results.md depuis eval/raw_*.jsonl

Métriques :
  - Retrieval@5   : l'article attendu figure-t-il parmi les 5 extraits récupérés ?
  - Citation      : la réponse cite-t-elle l'article attendu ?
  - Fidélité      : chaque affirmation est-elle appuyée par les extraits ? (LLM juge)
  - Refus correct : « je ne sais pas » sur les questions pièges
  - Faux refus    : « je ne sais pas » alors que la réponse est dans le texte
  - Latence et coût
"""
import argparse
import json
import re
from pathlib import Path
from statistics import mean

from app.llm.base import LLMProvider, get_provider
from app.rag.answer import Answer, answer

EVAL_DIR = Path(__file__).parent
QUESTIONS = EVAL_DIR / "questions.jsonl"
RESULTS = EVAL_DIR / "results.md"

JUDGE_SYSTEM = """Tu es un évaluateur strict. On te donne des extraits d'un texte de loi et une réponse.
Tu évalues uniquement la FIDÉLITÉ : la réponse contient-elle une affirmation qui n'est PAS appuyée par les extraits,
ou qui les contredit ?
- Une affirmation absente des extraits, même vraie dans l'absolu, rend la réponse non fidèle.
- Une reformulation ou un résumé fidèle des extraits est acceptable.
- Une réponse INCOMPLÈTE n'est PAS une faute de fidélité : n'évalue pas l'exhaustivité.
Réponds uniquement en JSON : {"fidele": true ou false, "raison": "une phrase citant l'affirmation fautive s'il y en a une"}"""


def label(article: str) -> str:
    return f"Article {article}" if article.isdigit() else article


def judge(a: Answer, judge_llm: LLMProvider) -> dict:
    excerpts = "\n\n".join(f"[{r.label}]\n{r.contenu}" for r in a.sources)
    prompt = f"Extraits :\n\n{excerpts}\n\n---\nQuestion : {a.question}\n\nRéponse à évaluer :\n{a.text}"
    raw = judge_llm.generate(prompt, system=JUDGE_SYSTEM).text
    m = re.search(r"\{.*\}", raw, re.DOTALL)
    try:
        return json.loads(m.group(0)) if m else {"fidele": None, "raison": raw[:200]}
    except json.JSONDecodeError:
        return {"fidele": None, "raison": raw[:200]}


def run(provider_name: str, questions: list[dict], judge_llm: LLMProvider) -> list[dict]:
    provider = get_provider(provider_name)
    records = []
    for i, q in enumerate(questions, 1):
        a = answer(q["question"], provider)
        expected = [label(e) for e in q["expected"]]
        retrieved = list(dict.fromkeys(r.label for r in a.sources))
        rec = {
            **q,
            "model": a.llm.model,
            "answer": a.text,
            "retrieved": retrieved,
            "cited": a.cited,
            "refused": a.refused,
            "retrieval_hit": any(e in retrieved for e in expected) if expected else None,
            "citation_ok": any(e in a.cited for e in expected) if expected else None,
            "latency_s": a.llm.latency_s,
            "input_tokens": a.llm.input_tokens,
            "output_tokens": a.llm.output_tokens,
            "cost_usd": a.llm.cost_usd,
        }
        # On ne juge la fidélité que des vraies réponses (un refus est fidèle par construction).
        if q["type"] != "piege" and not a.refused:
            rec["judge"] = judge(a, judge_llm)
        records.append(rec)
        print(f"  [{i:2}/{len(questions)}] {q['id']} {a.llm.latency_s:5.1f}s "
              f"retrieval={rec['retrieval_hit']} citation={rec['citation_ok']} refus={a.refused} "
              f"fidèle={rec.get('judge', {}).get('fidele')}", flush=True)
    return records


def pct(values: list[bool]) -> str:
    values = [v for v in values if v is not None]
    return f"{100 * sum(values) / len(values):.0f} % ({sum(values)}/{len(values)})" if values else "n/a"


def summarize(records: list[dict], provider: str, human: dict[str, bool]) -> dict[str, str]:
    answerable = [r for r in records if r["type"] != "piege"]
    traps = [r for r in records if r["type"] == "piege"]
    judged = [r for r in answerable if "judge" in r]
    reviewed = [r for r in judged if f"{provider}/{r['id']}" in human]
    cost_per_q = mean(r["cost_usd"] for r in records)
    return {
        "Retrieval@5": pct([r["retrieval_hit"] for r in answerable]),
        "Citation de l'article attendu": pct([r["citation_ok"] for r in answerable]),
        "Fidélité (vérification humaine)": pct([human[f"{provider}/{r['id']}"] for r in reviewed]),
        "Fidélité (LLM juge)": pct([r["judge"].get("fidele") for r in judged]),
        "Accord juge / humain": pct([r["judge"].get("fidele") is human[f"{provider}/{r['id']}"] for r in reviewed]),
        "Refus correct (pièges)": pct([r["refused"] for r in traps]),
        "Faux refus (réponse existante)": pct([r["refused"] for r in answerable]),
        "Latence moyenne": f"{mean(r['latency_s'] for r in records):.1f} s",
        "Tokens moyens (entrée + sortie)": f"{mean(r['input_tokens'] for r in records):.0f} + "
                                           f"{mean(r['output_tokens'] for r in records):.0f}",
        "Coût pour 1 000 questions": f"{1000 * cost_per_q:.2f} $",
    }


def write_report(all_records: dict[str, list[dict]], judge_model: str) -> None:
    models = {name: recs[0]["model"] for name, recs in all_records.items()}
    from eval.manual_review import read_verdicts
    human = read_verdicts()
    summaries = {name: summarize(recs, name, human) for name, recs in all_records.items()}
    metrics = next(iter(summaries.values())).keys()

    lines = [
        "# Résultats de l'évaluation",
        "",
        f"{len(next(iter(all_records.values())))} questions (`eval/questions.jsonl`) : "
        "questions simples, cas d'usage à classer et questions pièges dont la réponse est absente du texte. "
        f"Juge de fidélité : `{judge_model}`.",
        "",
        "La fidélité humaine provient de `eval/manual_review.md` : avis pré-remplis par Claude "
        "(chaque affirmation confrontée aux extraits fournis au modèle), relus et validés par l'auteur. "
        "L'accord juge / humain mesure la fiabilité du LLM juge lui-même.",
        "",
        "| Métrique | " + " | ".join(f"`{m}`" for m in models.values()) + " |",
        "|---|" + "---|" * len(models),
    ]
    for metric in metrics:
        lines.append(f"| {metric} | " + " | ".join(summaries[n][metric] for n in models) + " |")

    lines += ["", "## Détail par question", "",
              "| Question | Type | Attendu | " + " | ".join(f"`{m}`" for m in models.values()) + " |",
              "|---|---|---|" + "---|" * len(models)]
    by_id = {n: {r["id"]: r for r in recs} for n, recs in all_records.items()}
    first = next(iter(all_records.values()))
    for q in first:
        cells = []
        for n in models:
            r = by_id[n][q["id"]]
            if r["type"] == "piege":
                cells.append("✅ refus" if r["refused"] else "❌ a répondu")
            else:
                fid = r.get("judge", {}).get("fidele")
                cells.append(("refus ❌" if r["refused"] else
                              f"cite {'✅' if r['citation_ok'] else '❌'} · fidèle {'✅' if fid else '❌' if fid is False else '?'}")
                             + f" · {r['latency_s']:.0f} s")
        expected = ", ".join(label(e) for e in q["expected"]) or "—"
        lines.append(f"| {q['question']} | {q['type']} | {expected} | " + " | ".join(cells) + " |")

    RESULTS.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n-> {RESULTS}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--providers", nargs="+", default=["ollama", "mistral"])
    parser.add_argument("--judge", default="mistral")
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()

    questions = [json.loads(l) for l in QUESTIONS.read_text(encoding="utf-8").splitlines() if l.strip()]
    judge_llm = get_provider(args.judge)

    if not args.report_only:
        for name in args.providers:
            print(f"== {name}")
            records = run(name, questions, judge_llm)
            with open(EVAL_DIR / f"raw_{name}.jsonl", "w", encoding="utf-8") as f:
                f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in records)

    all_records = {}
    for name in ["ollama", "mistral"]:
        path = EVAL_DIR / f"raw_{name}.jsonl"
        if path.exists():
            all_records[name] = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines()]
    write_report(all_records, getattr(judge_llm, "model", args.judge))


if __name__ == "__main__":
    main()
