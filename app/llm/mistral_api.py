import time

import httpx

from app.config import settings
from app.llm.base import LLMProvider, LLMResponse


class MistralAPIProvider(LLMProvider):
    """Modèle cloud via l'API Mistral (La Plateforme).

    La formule gratuite ne facture rien, mais on calcule le coût au tarif payant
    (MISTRAL_PRICE_* dans le .env) pour que la comparaison local/cloud reste parlante.
    """

    name = "mistral"
    MAX_RETRIES = 5

    def __init__(self) -> None:
        if not settings.mistral_api_key:
            raise RuntimeError("MISTRAL_API_KEY manquante dans le .env")
        self.model = settings.mistral_model
        self.client = httpx.Client(
            base_url="https://api.mistral.ai/v1",
            headers={"Authorization": f"Bearer {settings.mistral_api_key}"},
            timeout=120,
        )

    def _post(self, payload: dict) -> httpx.Response:
        # La formule gratuite est limitée en débit : on réessaie sur 429 avec un délai croissant.
        for attempt in range(self.MAX_RETRIES):
            r = self.client.post("/chat/completions", json=payload)
            if r.status_code != 429:
                r.raise_for_status()
                return r
            time.sleep(2 ** attempt)
        r.raise_for_status()
        return r

    def generate(self, prompt: str, system: str | None = None, json_mode: bool = False) -> LLMResponse:
        messages = [{"role": "system", "content": system}] if system else []
        messages.append({"role": "user", "content": prompt})

        start = time.perf_counter()
        payload = {"model": self.model, "messages": messages, "temperature": 0}
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        data = self._post(payload).json()
        latency = time.perf_counter() - start

        usage = data["usage"]
        cost = (usage["prompt_tokens"] * settings.mistral_price_input_per_m
                + usage["completion_tokens"] * settings.mistral_price_output_per_m) / 1_000_000
        return LLMResponse(
            text=data["choices"][0]["message"]["content"],
            model=f"mistral/{self.model}",
            input_tokens=usage["prompt_tokens"],
            output_tokens=usage["completion_tokens"],
            latency_s=latency,
            cost_usd=cost,
        )
