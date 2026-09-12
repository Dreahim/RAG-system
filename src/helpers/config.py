from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    # File config
    FILE_ALLOWED_TYPES: str
    FILE_MAX_SIZE_MB: int
    FILE_DEFAULT_CHUNK_SIZE: int

    # Database config
    MONGODB_URL: str
    MONGODB_DB_NAME: str

    # LLM config
    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str

    OPENAI_API_KEY: str
    OPENAI_API_URL: str

    COHERE_API_KEY: str

    GENERATION_MODEL_ID: str
    EMBEDDING_MODEL_ID: str
    EMBEDDING_MODEL_SIZE: int

    DEFAULT_INPUT_MAX_CHARACTER: int
    DEFAULT_GENERATION_MAX_OUTPUT_TOKENS: int
    DEFAULT_GENERATION_TEMPERATURE: float

    model_config = SettingsConfigDict(
        env_file=".env",
    )


def get_settings():
    return Settings()