# api/routes/chat.py

from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from api.schemas.chat import (
    ChatRequest,
    ChatResponse,
    ErrorResponse
)

from api.services.rag_service import RAGService

from api.dependencies import (
    get_rag_service
)

import dotenv
dotenv.load_dotenv()

from api.core.logging import get_logger

logger = get_logger(__name__)

# ---------------------------------------------------
# Router
# ---------------------------------------------------

router = APIRouter(
    prefix="/chat",
    tags=["RAG Chat"]
)


# ---------------------------------------------------
# Chat Endpoint
# ---------------------------------------------------

@router.post(
    "/ask",

    response_model=ChatResponse,

    responses={
        500: {
            "model": ErrorResponse
        }
    }
)
def ask_question(
    payload: ChatRequest,

    rag_service: RAGService = Depends(
        get_rag_service
    )
):

    try:

        response = rag_service.ask(
            query=payload.query,
            top_k=payload.top_k,
            include_sources=payload.include_sources
        )

        return response

    except Exception as e:

        logger.exception(
            "Error occurred while processing chat request."
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )