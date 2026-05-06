# rag/retriever.py

import numpy as np

from openai import OpenAI
from dotenv import load_dotenv
import os

from rag.vector_store import load_faiss_index

# Load environment variables
load_dotenv(override=True)

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Embedding model
EMBEDDING_MODEL = "text-embedding-3-small"


def create_query_embedding(query):
    """
    Convert user query into embedding vector.
    """

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=query
    )

    embedding = response.data[0].embedding

    return embedding


def retrieve_chunks(query,
                    index,
                    embedded_chunks,
                    top_k=5):
    """
    Retrieve most relevant chunks
    from FAISS index.
    """

    # ---------------------------------
    # Create Query Embedding
    # ---------------------------------
    query_embedding = create_query_embedding(
        query
    )

    # Convert to NumPy array
    query_vector = np.array(
        [query_embedding],
        dtype="float32"
    )

    # ---------------------------------
    # Search FAISS Index
    # ---------------------------------
    distances, indices = index.search(
        query_vector,
        top_k
    )

    # ---------------------------------
    # Collect Results
    # ---------------------------------
    results = []

    for rank, idx in enumerate(indices[0]):

        retrieved_chunk = embedded_chunks[idx]

        results.append({
            "rank": rank + 1,
            "distance": float(
                distances[0][rank]
            ),
            "chunk": retrieved_chunk
        })

    return results