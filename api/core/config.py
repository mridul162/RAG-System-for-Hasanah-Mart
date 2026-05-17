# api/core/config.py


from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache
import dotenv
dotenv.load_dotenv()


class Settings(BaseSettings):

    # -------------------------------------------------
    # APP INFO
    # -------------------------------------------------

    app_name: str = "Hasanah Mart RAG API"

    app_version: str = "1.0.0"

    debug: bool = True


    # -------------------------------------------------
    # OPENAI
    # -------------------------------------------------

    openai_api_key: str = Field(
        ...,
        alias="OPENAI_API_KEY"
    )

    chat_model: str = "gpt-4.1-mini"

    embedding_model: str = (
        "text-embedding-3-small"
    )

    temperature: float = 0.2


    # -------------------------------------------------
    # WHATSAPP
    # -------------------------------------------------

    whatsapp_verify_token: str = Field(
        ...,
        alias="WHATSAPP_VERIFY_TOKEN"
    )

    whatsapp_access_token: str = Field(
        ...,
        alias="WHATSAPP_ACCESS_TOKEN"
    )

    whatsapp_phone_number_id: str = Field(
        ...,
        alias="WHATSAPP_PHONE_NUMBER_ID"
    )


    # -------------------------------------------------
    # VECTOR DATABASE
    # -------------------------------------------------

    faiss_index_path: str = (
        "vector_db/faiss_index.index"
    )

    metadata_path: str = (
        "vector_db/chunks_metadata.pkl"
    )


    # -------------------------------------------------
    # RETRIEVAL
    # -------------------------------------------------

    default_top_k: int = 5

    max_top_k: int = 10


    # -------------------------------------------------
    # CHUNKING
    # -------------------------------------------------

    chunk_size: int = 500

    chunk_overlap: int = 100


    # -------------------------------------------------
    # PROMPTING
    # -------------------------------------------------

    max_context_chars: int = 4000


    # -------------------------------------------------
    # CORS
    # -------------------------------------------------

    allowed_origins: list[str] = [
        "*"
    ]


    # -------------------------------------------------
    # PYDANTIC CONFIG
    # -------------------------------------------------

    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

    # -------------------------------------------------     
    # PostgreQSL CONFIG 
    # -------------------------------------------------
    database_url: str = Field(
        ...,
        alias="DATABASE_URL"
    )


# -----------------------------------------------------
# Cached Settings Instance
# -----------------------------------------------------

@lru_cache
def get_settings():

    return Settings()


# -----------------------------------------------------
# Global Settings Object
# -----------------------------------------------------

settings = get_settings()