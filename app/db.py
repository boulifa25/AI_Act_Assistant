import psycopg
from pgvector.psycopg import register_vector

from app.config import settings

SCHEMA = f"""
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS chunks (
    id        SERIAL PRIMARY KEY,
    article   TEXT NOT NULL,          -- "5", "6", "Annexe III", "Considérant"...
    titre     TEXT,
    chapitre  TEXT,
    contenu   TEXT NOT NULL,
    embedding vector({settings.embedding_dim}),
    tsv       tsvector GENERATED ALWAYS AS (to_tsvector('french', coalesce(titre, '') || ' ' || contenu)) STORED
);

CREATE INDEX IF NOT EXISTS chunks_tsv_idx ON chunks USING GIN (tsv);
CREATE INDEX IF NOT EXISTS chunks_embedding_idx ON chunks USING hnsw (embedding vector_cosine_ops);
"""


def connect() -> psycopg.Connection:
    conn = psycopg.connect(settings.db_url, autocommit=True)
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    register_vector(conn)
    return conn


def init_db(conn: psycopg.Connection) -> None:
    conn.execute(SCHEMA)
