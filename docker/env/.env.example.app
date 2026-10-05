APP_NAME="RAG-system"
APP_VERSION="0.2.0"
FILE_ALLOWED_TYPES="text/plain,application/pdf"
FILE_MAX_SIZE_MB=10
FILE_DEFAULT_CHUNK_SIZE=512000 # 512 kb

POSTGRES_USERNAME="postgres"
POSTGRES_PASSWORD="postgres_password"
POSTGRES_HOST="pgvector"
POSTGRES_PORT=5432
POSTGRES_MAIN_DATABASE="ragsystem"

# ======================== LLM config ========================
GENERATION_BACKEND="OPENAI"
EMBEDDING_BACKEND="OPENAI"

OPENAI_API_KEY="YOUR_SECRET_KEY_HERE"
OPENAI_API_URL=
COHERE_API_KEY="YOUR_SECRET_KEY_HERE"

GENERATION_MODEL_ID_LITERAL=["qwen2.5:3b-instruct-q3_K_S", "gpt-4o-mini"]
GENERATION_MODEL_ID="gpt-4o-mini"
EMBEDDING_MODEL_ID="text-embedding-3-small" # text-embedding-3-small , embed-multilingual-v3.0
EMBEDDING_MODEL_SIZE=1536

DEFAULT_INPUT_MAX_CHARACTER=1024
DEFAULT_GENERATION_MAX_OUTPUT_TOKENS=200
DEFAULT_GENERATION_TEMPERATURE=0.1

# ===================== Vector DB config =====================
VECTOR_DB_BACKEND_LITERAL=["QDRANT", "PGVECTOR"]
VECTOR_DB_BACKEND="PGVECTOR"
VECTOR_DB_PATH="qdrant_db"
VECTOR_DB_DISTANCE_METHOD="cosine"
VECTOR_DB_PGVEC_INDEX_THRESHOLD = 500

# ===================== Template Configs =====================
DEFAULT_LANG="ar"