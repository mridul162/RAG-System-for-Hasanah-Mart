# api/app.py

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.chat import router as chat_router
from api.services.rag_service import RAGService
from api.core.config import settings


# ---------------------------------------------------
# Application Lifespan
# ---------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    # ---------------------------------------------
    # Startup
    # ---------------------------------------------
    print("\n" + "=" * 60)
    print(
    f"STARTING {settings.app_name} "
    f"v{settings.app_version}"
    )
    print("=" * 60)

    # Initialize shared RAG service
    app.state.rag_service = RAGService()

    print("RAG service initialized!")

    yield

    # ---------------------------------------------
    # Shutdown
    # ---------------------------------------------
    print("\n" + "=" * 60)
    print("SHUTTING DOWN API")
    print("=" * 60)


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