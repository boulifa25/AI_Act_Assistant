from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    db_url: str = "postgresql://aiact:aiact@localhost:5433/aiact"
    embedding_model: str = "intfloat/multilingual-e5-small"
    embedding_dim: int = 384
    pdf_path: str = "data/ai_act_fr.pdf"

    llm_provider: str = "mistral"
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "mistral"
    ollama_num_ctx: int = 6144  # la classification envoie l'annexe III entière (~2 400 tokens)
    mistral_api_key: str = ""
    mistral_model: str = "ministral-14b-latest"
    # Tarif payant en $ par million de tokens (à vérifier sur mistral.ai/pricing)
    mistral_price_input_per_m: float = 0.2
    mistral_price_output_per_m: float = 0.2


settings = Settings()
