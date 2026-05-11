# api/services/whatsapp_service.py

import requests

from api.core.config import settings
from api.core.logging import get_logger


logger = get_logger(__name__)


def send_whatsapp_message(
    to_number: str,
    message: str
):

    url = (
        "https://graph.facebook.com/v22.0/"
        f"{settings.whatsapp_phone_number_id}"
        "/messages"
    )

    headers = {
        "Authorization": (
            f"Bearer "
            f"{settings.whatsapp_access_token}"
        ),

        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",

        "to": to_number,

        "type": "text",

        "text": {
            "body": message
        }
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=payload,
        timeout=30
    )

    logger.info(
        f"WhatsApp send response: "
        f"{response.status_code}"
    )

    logger.info(response.text)

    return response.json()