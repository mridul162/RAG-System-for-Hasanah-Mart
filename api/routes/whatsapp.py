# api/routes/whatsapp.py

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import PlainTextResponse

from api.core.config import settings


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