from pydantic import BaseModel

from datetime import datetime


class ConversationResponse(BaseModel):

    id: int

    phone_number: str

    user_message: str

    ai_response: str

    created_at: datetime

    class Config:

        from_attributes = True


class AnalyticsResponse(BaseModel):

    total_conversations: int

    total_users: int