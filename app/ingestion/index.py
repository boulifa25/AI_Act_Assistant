"""Pipeline complet : PDF -> chunks -> embeddings -> pgvector.

Usage : python -m app.ingestion.index
"""
from functools import lru_cache

from sentence_transformers import SentenceTransformer

from app.config import settings
from app.db import connect, init_db
from app.ingestion.chunk import Chunk, chunk_text
from app.ingestion.parse import extract_text


@lru_cache
def get_model() -> SentenceTransformer:
    return SentenceTransformer(settings.embedding_model)


def passage_text(c: Chunk) -> str:
    # Les modèles e5 attendent le préfixe "passage: " (et "query: " côté requête).
    # On injecte l'en-tête (article + titre) pour que chaque sous-chunk garde son contexte.
    head = f"Article {c.article}" if c.article.isdigit() else c.article
    if c.titre:
        head += f" — {c.titre}"
    return f"passage: {head}\n{c.contenu}"


def embed_query(query: str) -> list[float]:
    return get_model().encode(f"query: {query}", normalize_embeddings=True).tolist()


def main() -> None:
    chunks = chunk_text(extract_text(settings.pdf_path))
    print(f"{len(chunks)} chunks, calcul des embeddings...")
    vectors = get_model().encode(
        [passage_text(c) for c in chunks],
        normalize_embeddings=True, batch_size=32, show_progress_bar=True,
    )

    with connect() as conn:
        init_db(conn)
        conn.execute("TRUNCATE chunks RESTART IDENTITY")
        with conn.cursor() as cur:
            cur.executemany(
                "INSERT INTO chunks (article, titre, chapitre, contenu, embedding) VALUES (%s, %s, %s, %s, %s)",
                [(c.article, c.titre, c.chapitre, c.contenu, v) for c, v in zip(chunks, vectors)],
            )
        n = conn.execute("SELECT count(*) FROM chunks").fetchone()[0]
    print(f"{n} chunks insérés.")


if __name__ == "__main__":
    main()
