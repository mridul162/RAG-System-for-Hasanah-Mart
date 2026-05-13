from sqlalchemy.orm import Session
from sqlalchemy import func

from api.db.models import Conversation


def get_conversations(
    db: Session,
    limit: int = 50
):

    return (
        db.query(Conversation)
        .order_by(
            Conversation.created_at.desc()
        )
        .limit(limit)
        .all()
    )


def get_conversation_by_id(
    db: Session,
    conversation_id: int
):

    return (
        db.query(Conversation)
        .filter(
            Conversation.id == conversation_id
        )
        .first()
    )


def get_dashboard_analytics(
    db: Session
):

    total_conversations = (
        db.query(Conversation)
        .count()
    )

    total_users = (
        db.query(
            func.count(
                func.distinct(
                    Conversation.phone_number
                )
            )
        )
        .scalar()
    )

    return {
        "total_conversations": (
            total_conversations
        ),

        "total_users": total_users
    }