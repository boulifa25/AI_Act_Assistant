import time

import httpx

from app.config import settings
from app.llm.base import LLMProvider, LLMResponse


class OllamaProvider(LLMProvider):
    """Modèle local servi par Ollama : coût nul, latence dépendante de la machine."""

    name = "ollama"

    def __init__(self) -> None:
        self.model = settings.ollama_model
        self.client = httpx.Client(base_url=settings.ollama_url, timeout=300)

    def generate(self, prompt: str, system: str | None = None) -> LLMResponse:
        messages = [{"role": "system", "content": system}] if system else []
        messages.append({"role": "user", "content": prompt})

        start = time.perf_counter()
        r = self.client.post("/api/chat", json={
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": 0, "num_ctx": settings.ollama_num_ctx},
        })
        r.raise_for_status()
        latency = time.perf_counter() - start
        data = r.json()

        return LLMResponse(
            text=data["message"]["content"],
            model=f"ollama/{self.model}",
            input_tokens=data.get("prompt_eval_count", 0),
            output_tokens=data.get("eval_count", 0),
            latency_s=latency,
            cost_usd=0.0,
        )
