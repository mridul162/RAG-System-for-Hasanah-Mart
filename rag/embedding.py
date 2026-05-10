# rag/embedding.py

from openai import OpenAI
from dotenv import load_dotenv
from rag.data_loader import load_documents
from rag.chunking import chunk_documents
from api.core.config import settings

import os
import time

# Load environment variables
load_dotenv(override=True)

# Initialize OpenAI client
client = OpenAI(
    api_key=settings.openai_api_key
)

# Embedding model
EMBEDDING_MODEL = settings.embedding_model


def create_embedding(text):
    """
    Create embedding for a single text chunk.
    """

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    embedding = response.data[0].embedding

    return embedding


def create_embeddings(chunks):
    """
    Generate embeddings for all chunks.
    """

    embedded_chunks = []

    total_chunks = len(chunks)

    print(f"\nGenerating embeddings for {total_chunks} chunks...\n")

    for i, chunk in enumerate(chunks):

        try:

            # Skip empty chunks
            if not chunk["content"].strip():
                continue

            embedding = create_embedding(
                chunk["content"]
            )

            embedded_chunks.append({
                "chunk_id": chunk["chunk_id"],
                "source": chunk["source"],
                "type": chunk["type"],
                "content": chunk["content"],
                "embedding": embedding
            })

            print(
                f"[{i+1}/{total_chunks}] "
                f"Embedded Chunk ID: {chunk['chunk_id']}"
            )

            # Small delay to reduce rate-limit risk
            time.sleep(0.1)

        except Exception as e:

            print(
                f"\nError embedding chunk "
                f"{chunk['chunk_id']}"
            )

            print(e)

    return embedded_chunks


