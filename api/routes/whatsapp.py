# api/routes/whatsapp.py

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import PlainTextResponse

from api.core.config import settings
from api.core.logging import get_logger
from api.services import rag_service
from api.services.whatsapp_service import (
    send_whatsapp_message
)


logger = get_logger(__name__)

router = APIRouter(
    prefix="/webhooks/whatsapp",
    tags=["WhatsApp"]
)


# ---------------------------------------------------
# Webhook Verification
# ---------------------------------------------------

@router.get("")

async def verify_webhook(request: Request):

    hub_mode = request.query_params.get(
        "hub.mode"
    )

    hub_verify_token = request.query_params.get(
        "hub.verify_token"
    )

    hub_challenge = request.query_params.get(
        "hub.challenge"
    )

    if (
        hub_mode == "subscribe"
        and
        hub_verify_token
        == settings.whatsapp_verify_token
    ):

        return PlainTextResponse(
            content=hub_challenge,
            status_code=200
        )

    return PlainTextResponse(
        content="Verification failed",
        status_code=403
    )

# ---------------------------------------------------
# Receive WhatsApp Events
# ---------------------------------------------------

@router.post("")

async def receive_whatsapp_message(
    request: Request
):

    payload = await request.json()

    logger.info(
        "Incoming WhatsApp webhook received."
    )

    logger.info(payload)

    try:

        message = (
            payload["entry"][0]
            ["changes"][0]
            ["value"]["messages"][0]
        )

        sender_number = message["from"]

        message_text = (
            message["text"]["body"]
        )

        logger.info(
            f"Message from "
            f"{sender_number}: "
            f"{message_text}"
        )

        # -----------------------------------------
        # Temporary Static Reply
        # -----------------------------------------

        send_whatsapp_message(
            to_number=sender_number,

            message=(
                rag_service.ask()
            )
        )

    except Exception as e:

        logger.error(str(e))

    return {
        "status": "received"
    }