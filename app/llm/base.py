"""Interface commune à tous les fournisseurs de LLM (pattern Adapter).

Le reste de l'application ne connaît que LLMProvider.generate() : changer de modèle
revient à changer LLM_PROVIDER dans le .env.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class LLMResponse:
    text: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_s: float
    cost_usd: float


class LLMProvider(ABC):
    name: str

    @abstractmethod
    def generate(self, prompt: str, system: str | None = None) -> LLMResponse:
        ...


def get_provider(name: str | None = None) -> LLMProvider:
    from app.config import settings

    name = name or settings.llm_provider
    if name == "ollama":
        from app.llm.ollama import OllamaProvider
        return OllamaProvider()
    if name == "mistral":
        from app.llm.mistral_api import MistralAPIProvider
        return MistralAPIProvider()
    raise ValueError(f"LLM_PROVIDER inconnu : {name!r} (attendu : ollama | mistral)")
