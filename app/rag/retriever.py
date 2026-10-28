"""Recherche hybride : similarité vectorielle (pgvector) + plein texte (tsvector),
fusionnées par Reciprocal Rank Fusion (RRF).

Usage : python -m app.rag.retriever "pratiques interdites"
"""
from dataclasses import dataclass

from app.db import connect
from app.ingestion.index import embed_query

RRF_K = 60  # constante standard de RRF
# Les considérants expliquent, les articles obligent : à pertinence égale, l'article passe devant.
# Mesuré sur eval/questions.jsonl : Retrieval@5 de 14/17 à 15/17.
RECITAL_WEIGHT = 0.5


@dataclass
class Result:
    id: int
    article: str
    titre: str | None
    chapitre: str | None
    contenu: str
    score: float

    @property
    def label(self) -> str:
        return f"Article {self.article}" if self.article.isdigit() else self.article


VECTOR_SQL = """
SELECT id, article FROM chunks ORDER BY embedding <=> %s::vector LIMIT %s
"""

FULLTEXT_SQL = """
SELECT id, article FROM chunks, websearch_to_tsquery('french', %s) q
WHERE tsv @@ q ORDER BY ts_rank_cd(tsv, q) DESC LIMIT %s
"""


def search(query: str, k: int = 5, candidates: int = 30, conn=None) -> list[Result]:
    own = conn is None
    conn = conn or connect()
    try:
        vec = conn.execute(VECTOR_SQL, (embed_query(query), candidates)).fetchall()
        ft = conn.execute(FULLTEXT_SQL, (query, candidates)).fetchall()

        scores: dict[int, float] = {}
        for ranking in (vec, ft):
            for rank, (cid, article) in enumerate(ranking):
                weight = RECITAL_WEIGHT if article.startswith("Considérant") else 1.0
                scores[cid] = scores.get(cid, 0.0) + weight / (RRF_K + rank + 1)

        top = sorted(scores, key=scores.get, reverse=True)[:k]
        if not top:
            return []
        rows = conn.execute(
            "SELECT id, article, titre, chapitre, contenu FROM chunks WHERE id = ANY(%s)", (top,)
        ).fetchall()
        by_id = {r[0]: r for r in rows}
        return [Result(*by_id[i], score=scores[i]) for i in top]
    finally:
        if own:
            conn.close()


if __name__ == "__main__":
    import sys

    q = " ".join(sys.argv[1:]) or "pratiques interdites"
    for i, r in enumerate(search(q, k=10), 1):
        print(f"{i:2}. [{r.score:.4f}] {r.label} — {r.titre or ''}")
