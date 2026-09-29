from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    # File config
    FILE_ALLOWED_TYPES: str
    FILE_MAX_SIZE_MB: int
    FILE_DEFAULT_CHUNK_SIZE: int

    # Database config
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_MAIN_DATABASE: str


    # LLM config
    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str

    OPENAI_API_KEY: str = None
    OPENAI_API_URL: str = None

    COHERE_API_KEY: str = None

    GENERATION_MODEL_ID_LITERAL: List[str] = None
    GENERATION_MODEL_ID: str = None
    EMBEDDING_MODEL_ID: str = None
    EMBEDDING_MODEL_SIZE: int = None

    DEFAULT_INPUT_MAX_CHARACTER: int = None
    DEFAULT_GENERATION_MAX_OUTPUT_TOKENS: int = None
    DEFAULT_GENERATION_TEMPERATURE: float = None

    # Vecor DB config
    VECTOR_DB_BACKEND_LITERAL: List[str]
    VECTOR_DB_BACKEND: str
    VECTOR_DB_PATH: str
    VECTOR_DB_DISTANCE_METHOD: str = None
    VECTOR_DB_PGVEC_INDEX_THRESHOLD:int = 100

    # Template Configs 
    DEFAULT_LANG: str ="en"

    model_config = SettingsConfigDict(
        env_file=".env",
    )


def get_settings():
    return Settings()