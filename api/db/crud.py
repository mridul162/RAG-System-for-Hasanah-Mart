from sqlalchemy.orm import Session

from api.db.models import Conversation


def save_conversation(
    db: Session,
    phone_number: str,
    user_message: str,
    ai_response: str
):

    conversation = Conversation(
        phone_number=phone_number,
        user_message=user_message,
        ai_response=ai_response
    )

    db.add(conversation)

    db.commit()

    db.refresh(conversation)

    return conversation