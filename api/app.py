# api/app.py

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.chat import router as chat_router
from api.routes.whatsapp import (
    router as whatsapp_router
)

from api.services.rag_service import RAGService

from api.core.config import settings
from api.core.logging import (
    setup_logging,
    get_logger
)


# ---------------------------------------------------
# Setup Logging
# ---------------------------------------------------

setup_logging()

logger = get_logger(__name__)


# ---------------------------------------------------
# Application Lifespan
# ---------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    # ---------------------------------------------
    # Startup
    # ---------------------------------------------

    logger.info(
        f"Starting {settings.app_name} "
        f"v{settings.app_version}"
    )

    # Initialize shared RAG service
    app.state.rag_service = RAGService()

    logger.info(
        "RAG service initialized successfully."
    )

    yield

    # ---------------------------------------------
    # Shutdown
    # ---------------------------------------------

    logger.info("Shutting down API.")


# ---------------------------------------------------
# FastAPI App
# ---------------------------------------------------

app = FastAPI(
    title=settings.app_name,

    description=(
        "RAG-powered AI assistant for "
        "Hasanah Mart organic food business."
    ),

    version=settings.app_version,

    debug=settings.debug,

    lifespan=lifespan
)


# ---------------------------------------------------
# CORS
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,

    allow_origins=settings.allowed_origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ---------------------------------------------------
# Root Endpoints
# ---------------------------------------------------

@app.get("/")
def root():

    return {
        "message": (
            f"{settings.app_name} is running."
        ),

        "version": settings.app_version
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy",

        "service": settings.app_name,

        "version": settings.app_version
    }


# ---------------------------------------------------
# Register Routers
# ---------------------------------------------------

app.include_router(chat_router)

app.include_router(whatsapp_router)