"""Vérification humaine de la fidélité, pour mesurer aussi la fiabilité du LLM juge.

  python -m eval.manual_review build   # génère eval/manual_review.md à relire
  python -m eval.manual_review score   # lit tes verdicts et met à jour results.md

Dans manual_review.md, remplace « ? » par OUI ou NON sur chaque ligne « Ton verdict ».
"""
import json
import re
import sys
from pathlib import Path

from app.rag.retriever import search

EVAL_DIR = Path(__file__).parent
REVIEW = EVAL_DIR / "manual_review.md"
PROPOSALS = EVAL_DIR / "review_proposals.json"
PROVIDERS = ["ollama", "mistral"]
VERDICT_RE = re.compile(r"^## (\w+)/(\w+) .*?^\*\*Ton verdict :\*\* (\S+)", re.MULTILINE | re.DOTALL)


def load_raw(provider: str) -> list[dict]:
    path = EVAL_DIR / f"raw_{provider}.jsonl"
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines()] if path.exists() else []


def build() -> None:
    proposals = json.loads(PROPOSALS.read_text(encoding="utf-8")) if PROPOSALS.exists() else {}
    out = ["# Vérification manuelle de la fidélité", "",
           "Question posée pour chaque réponse : **contient-elle une affirmation absente des extraits "
           "ou qui les contredit ?** Une réponse incomplète reste fidèle.", "",
           "Remplace `?` par `OUI` (fidèle) ou `NON` sur chaque ligne « Ton verdict », "
           "puis lance `python -m eval.manual_review score`.", ""]
    for provider in PROVIDERS:
        for r in load_raw(provider):
            if "judge" not in r:
                continue
            key = f"{provider}/{r['id']}"
            judge = r["judge"].get("fidele")
            proposal, reason = proposals.get(key, ("?", ""))
            excerpts = "\n\n".join(f"**[{x.label}]**\n{x.contenu}" for x in search(r["question"], k=5))
            out += [
                f"## {key} — {r['question']}", "",
                f"**Réponse du modèle :**\n\n{r['answer'].strip()}", "",
                f"<details><summary>Extraits fournis au modèle</summary>\n\n{excerpts}\n\n</details>", "",
                f"- Juge 14B : {'OUI' if judge else 'NON' if judge is False else 'illisible'} — {r['judge'].get('raison', '')[:200]}",
                f"- Avis proposé par Claude : {proposal} — {reason}", "",
                "**Ton verdict :** ?", "", "---", "",
            ]
    REVIEW.write_text("\n".join(out), encoding="utf-8")
    print(f"-> {REVIEW}")


def read_verdicts() -> dict[str, bool]:
    """{"ollama/s01": True, ...} pour les verdicts renseignés (OUI/NON)."""
    if not REVIEW.exists():
        return {}
    verdicts = {}
    for provider, qid, v in VERDICT_RE.findall(REVIEW.read_text(encoding="utf-8")):
        if v.upper() in ("OUI", "NON"):
            verdicts[f"{provider}/{qid}"] = v.upper() == "OUI"
    return verdicts


def score() -> None:
    verdicts = read_verdicts()
    total = sum(1 for p in PROVIDERS for r in load_raw(p) if "judge" in r)
    print(f"{len(verdicts)}/{total} verdicts renseignés")
    from eval.run_eval import main as run_eval_main
    sys.argv = ["run_eval", "--report-only"]
    run_eval_main()


if __name__ == "__main__":
    {"build": build, "score": score}[sys.argv[1] if len(sys.argv) > 1 else "build"]()
