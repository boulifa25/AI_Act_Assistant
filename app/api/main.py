"""API HTTP de l'assistant.

  POST /ask       question libre : l'agent route vers la recherche ou la classification
  POST /classify  description d'un système d'IA -> niveau de risque
  GET  /health    état de la base et du fournisseur LLM

Lancement local : uvicorn app.api.main:app --reload   (doc interactive : /docs)
"""
from contextlib import asynccontextmanager
from functools import lru_cache
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.agent.graph import AgentState, build_graph
from app.config import settings
from app.db import connect, init_db
from app.ingestion.index import get_model
from app.llm.base import get_provider

Provider = Literal["ollama", "mistral"]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Premier lancement (docker compose up sur une base vide) : on indexe le PDF s'il est présent.
    with connect() as conn:
        init_db(conn)
        empty = conn.execute("SELECT count(*) FROM chunks").fetchone()[0] == 0
    if empty and Path(settings.pdf_path).exists():
        from app.ingestion.index import main as ingest
        ingest()
    get_model()  # charge le modèle d'embeddings une fois pour toutes
    yield


app = FastAPI(
    title="AI Act Assistant",
    description="Questions et classification du risque selon le règlement (UE) 2024/1689. "
                "Outil indicatif : ne remplace pas un avis juridique.",
    version="1.0.0",
    lifespan=lifespan,
)


@lru_cache
def graph_for(provider: str):
    return build_graph(get_provider(provider))


# --- Schémas ----------------------------------------------------------------------------

class AskRequest(BaseModel):
    question: str = Field(..., min_length=3, examples=["Quelles pratiques d'IA sont interdites ?"])
    provider: Provider | None = Field(None, description="Par défaut : LLM_PROVIDER du .env")


class ClassifyRequest(BaseModel):
    description: str = Field(..., min_length=3, examples=["Un chatbot RH qui trie des CV"])
    provider: Provider | None = None


class Source(BaseModel):
    article: str
    titre: str | None
    extrait: str


class Metrics(BaseModel):
    model: str | None
    llm_calls: int
    latency_s: float
    cost_usd: float


class AskResponse(BaseModel):
    route: Literal["question", "classification"]
    answer: str
    cited: list[str]
    sources: list[Source]
    metrics: Metrics


class ClassifyResponse(BaseModel):
    niveau: str
    justification: str
    verifications: dict
    articles: list[str]
    sources: list[Source]
    metrics: Metrics


# --- Helpers ----------------------------------------------------------------------------

def invoke(text: str, mode: str, provider: str | None) -> AgentState:
    try:
        return graph_for(provider or settings.llm_provider).invoke(
            {"input": text, "mode": mode, "llm_calls": []})
    except Exception as e:  # LLM injoignable, quota dépassé...
        raise HTTPException(status_code=502, detail=f"Erreur du fournisseur LLM : {e}") from e


def sources_of(state: AgentState) -> list[Source]:
    seen, out = set(), []
    for r in state.get("sources", []):
        if r.id not in seen:
            seen.add(r.id)
            out.append(Source(article=r.label, titre=r.titre, extrait=r.contenu[:400]))
    return out


def metrics_of(state: AgentState) -> Metrics:
    calls = state.get("llm_calls", [])
    return Metrics(
        model=calls[-1].model if calls else None,
        llm_calls=len(calls),
        latency_s=round(sum(c.latency_s for c in calls), 2),
        cost_usd=round(sum(c.cost_usd for c in calls), 6),
    )


# --- Routes -----------------------------------------------------------------------------

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest) -> AskResponse:
    s = invoke(req.question, "auto", req.provider)
    return AskResponse(route=s["route"], answer=s["answer"], cited=s.get("cited", []),
                       sources=sources_of(s), metrics=metrics_of(s))


@app.post("/classify", response_model=ClassifyResponse)
def classify(req: ClassifyRequest) -> ClassifyResponse:
    s = invoke(req.description, "classification", req.provider)
    c = s["classification"]
    return ClassifyResponse(**c, sources=sources_of(s), metrics=metrics_of(s))


@app.get("/health")
def health() -> dict:
    try:
        with connect() as conn:
            chunks = conn.execute("SELECT count(*) FROM chunks").fetchone()[0]
        db = "ok"
    except Exception as e:
        chunks, db = 0, f"erreur : {e}"
    return {"status": "ok" if db == "ok" and chunks else "degraded",
            "database": db, "chunks": chunks, "llm_provider": settings.llm_provider}
