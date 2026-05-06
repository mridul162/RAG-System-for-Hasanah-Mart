# rag/chunking.py

from rag.data_loader import load_documents


def chunk_text(text, chunk_size=500, chunk_overlap=100):
    """
    Split a single text into overlapping chunks.
    """

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        # Move start forward with overlap
        start += (chunk_size - chunk_overlap)

    return chunks


def chunk_documents(documents,
                    chunk_size=500,
                    chunk_overlap=100):
    """
    Chunk all loaded documents.
    """

    all_chunks = []

    chunk_id = 0

    for doc in documents:

        # -----------------------------
        # Handle Markdown Content
        # -----------------------------
        if doc["type"] == "markdown":

            text = doc["content"]

        # -----------------------------
        # Handle JSON Content
        # -----------------------------
        elif doc["type"] == "json":

            text = str(doc["content"])

        else:
            continue

        # Create chunks
        chunks = chunk_text(
            text=text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        # Store chunk metadata
        for chunk in chunks:

            all_chunks.append({
                "chunk_id": chunk_id,
                "source": doc["source"],
                "type": doc["type"],
                "content": chunk
            })

            chunk_id += 1

    return all_chunks


# ---------------------------------------------------
# Debugging / Testing
# ---------------------------------------------------

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