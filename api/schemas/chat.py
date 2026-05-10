# api/schemas/chat.py

from typing import List, Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------
# REQUEST SCHEMA
# ---------------------------------------------------

class ChatRequest(BaseModel):
    """
    Incoming user query payload.
    """

    query: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="User question for the RAG system."
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=10,
        description="Number of chunks to retrieve."
    )

    include_sources: bool = Field(
        default=True,
        description="Whether to include retrieved sources."
    )


# ---------------------------------------------------
# SOURCE SCHEMA
# ---------------------------------------------------

class SourceInfo(BaseModel):
    """
    Information about retrieved sources.
    """

    source: str = Field(
        ...,
        description="Original document source path."
    )

    chunk_id: int = Field(
        ...,
        description="Retrieved chunk ID."
    )

    distance: float = Field(
        ...,
        description="FAISS similarity distance."
    )

    preview: str = Field(
        ...,
        description="Preview of retrieved chunk."
    )


# ---------------------------------------------------
# RESPONSE SCHEMA
# ---------------------------------------------------

class ChatResponse(BaseModel):
    """
    Final API response.
    """

    query: str = Field(
        ...,
        description="Original user query."
    )

    answer: str = Field(
        ...,
        description="Generated RAG answer."
    )

    sources: Optional[List[SourceInfo]] = Field(
        default=None,
        description="Retrieved source chunks."
    )


# ---------------------------------------------------
# ERROR RESPONSE
# ---------------------------------------------------

class ErrorResponse(BaseModel):
    """
    Standard API error response.
    """

    error: str = Field(
        ...,
        description="Error message."
    )

    details: Optional[str] = Field(
        default=None,
        description="Additional error details."
    )