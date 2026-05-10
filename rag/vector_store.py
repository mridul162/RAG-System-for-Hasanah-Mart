# rag/vector_store.py

import faiss
import numpy as np
import pickle

from rag.data_loader import load_documents
from rag.chunking import chunk_documents
from rag.embedding import create_embeddings
from api.core.config import settings


def create_faiss_index(embedded_chunks):
    """
    Create FAISS index from embeddings.
    """

    # Extract embeddings
    embeddings = [
        chunk["embedding"]
        for chunk in embedded_chunks
    ]

    # Convert to NumPy array
    embeddings_array = np.array(
        embeddings,
        dtype="float32"
    )

    # Get embedding dimension
    dimension = embeddings_array.shape[1]

    print("\n" + "=" * 60)
    print(f"Embedding Dimension: {dimension}")
    print(f"Total Vectors       : {len(embeddings_array)}")
    print("=" * 60)

    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to index
    index.add(embeddings_array)

    print("\nFAISS index created successfully!")

    return index


def save_faiss_index(index,
                     embedded_chunks,
                     index_path=settings.faiss_index_path,
                     metadata_path=settings.metadata_path):
    """
    Save FAISS index and metadata.
    """

    # Save FAISS index
    faiss.write_index(index, index_path)

    # Save metadata separately
    with open(metadata_path, "wb") as f:
        pickle.dump(embedded_chunks, f)

    print("\nFAISS index saved!")
    print(f"Index Path    : {index_path}")
    print(f"Metadata Path : {metadata_path}")


def load_faiss_index(index_path=settings.faiss_index_path,
                     metadata_path=settings.metadata_path):
    """
    Load FAISS index and metadata.
    """

    # Load FAISS index
    index = faiss.read_index(index_path)

    # Load metadata
    with open(metadata_path, "rb") as f:
        embedded_chunks = pickle.load(f)

    print("\nFAISS index loaded successfully!")

    return index, embedded_chunks


