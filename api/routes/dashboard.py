from http.client import HTTPException

from fastapi import APIRouter, Depends
from requests import Session
from api.db.dependencies import (
    get_db
)

from api.db.crud import (
    get_conversations,
    get_conversation_by_id,
    get_dashboard_analytics
)

from api.schemas.dashboard import (
    ConversationResponse,
    AnalyticsResponse
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


# ---------------------------------------------------
# Get Conversations
# ---------------------------------------------------

@router.get(
    "/conversations",
    response_model=list[
        ConversationResponse
    ]
)
def fetch_conversations(
    db: Session = Depends(get_db)
):

    return get_conversations(db)


# ---------------------------------------------------
# Get Single Conversation
# ---------------------------------------------------

@router.get(
    "/conversations/{conversation_id}",
    response_model=ConversationResponse
)
def fetch_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):

    conversation = (
        get_conversation_by_id(
            db,
            conversation_id
        )
    )

    if not conversation:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return conversation


# ---------------------------------------------------
# Dashboard Analytics
# ---------------------------------------------------

@router.get(
    "/analytics",
    response_model=AnalyticsResponse
)
def fetch_dashboard_analytics(
    db: Session = Depends(get_db)
):

    return get_dashboard_analytics(db)