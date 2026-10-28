from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    db_url: str = "postgresql://aiact:aiact@localhost:5433/aiact"
    embedding_model: str = "intfloat/multilingual-e5-small"
    embedding_dim: int = 384
    pdf_path: str = "data/ai_act_fr.pdf"

    llm_provider: str = "ollama"
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "mistral"
    bedrock_model_id: str = "mistral.mistral-large-2402-v1:0"
    aws_region: str = "eu-west-3"


settings = Settings()
