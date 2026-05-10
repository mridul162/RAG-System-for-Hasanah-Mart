# api/app.py

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.chat import router as chat_router
from api.services.rag_service import RAGService


# ---------------------------------------------------
# Application Lifespan
# ---------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    # ---------------------------------------------
    # Startup
    # ---------------------------------------------
    print("\n" + "=" * 60)
    print("STARTING HASANAH MART RAG API")
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
    title="Hasanah Mart RAG API",

    description=(
        "RAG-powered AI assistant for "
        "Hasanah Mart organic food business."
    ),

    version="1.0.0",

    lifespan=lifespan
)


# ---------------------------------------------------
# CORS
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

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
            "Hasanah Mart RAG API is running."
        )
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# ---------------------------------------------------
# Register Routers
# ---------------------------------------------------

app.include_router(chat_router)