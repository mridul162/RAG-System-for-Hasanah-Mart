# ---------------------------------------------------
# Debugging / Testing chunking.py
# ---------------------------------------------------

from rag.chunking import chunk_documents
from rag.data_loader import load_documents


if __name__ == "__main__":

    documents = load_documents()

    chunks = chunk_documents(
        documents,
        chunk_size=500,
        chunk_overlap=100
    )

    print("\n" + "=" * 60)
    print(f"Total Chunks Created: {len(chunks)}")
    print("=" * 60)

    # Print sample chunks
    for chunk in chunks[:5]:

        print(f"\nChunk ID : {chunk['chunk_id']}")
        print(f"Source   : {chunk['source']}")
        print(f"Type     : {chunk['type']}")

        print("\nChunk Content:\n")
        print(chunk["content"])

        print("\n" + "-" * 60)