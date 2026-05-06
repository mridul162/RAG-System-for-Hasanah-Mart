# main.py

from rag.data_loader import load_documents
from rag.chunking import chunk_documents
from rag.embedding import create_embeddings

from rag.vector_store import (
    create_faiss_index,
    save_faiss_index,
    load_faiss_index
)

from rag.retriever import retrieve_chunks
from rag.prompt_builder import build_prompt
from rag.generator import generate_answer


# ---------------------------------------------------
# BUILD VECTOR DATABASE
# ---------------------------------------------------

def build_vector_database():

    print("\n" + "=" * 60)
    print("BUILDING VECTOR DATABASE")
    print("=" * 60)

    # ---------------------------------
    # Load Documents
    # ---------------------------------
    print("\nLoading documents...")

    documents = load_documents()

    print(
        f"Loaded {len(documents)} documents."
    )

    # ---------------------------------
    # Chunk Documents
    # ---------------------------------
    print("\nChunking documents...")

    chunks = chunk_documents(
        documents,
        chunk_size=500,
        chunk_overlap=100
    )

    print(
        f"Created {len(chunks)} chunks."
    )

    # ---------------------------------
    # Create Embeddings
    # ---------------------------------
    print("\nGenerating embeddings...")

    embedded_chunks = create_embeddings(
        chunks
    )

    print(
        f"Generated embeddings for "
        f"{len(embedded_chunks)} chunks."
    )

    # ---------------------------------
    # Create FAISS Index
    # ---------------------------------
    print("\nCreating FAISS index...")

    index = create_faiss_index(
        embedded_chunks
    )

    # ---------------------------------
    # Save Index
    # ---------------------------------
    print("\nSaving vector database...")

    save_faiss_index(
        index=index,
        embedded_chunks=embedded_chunks
    )

    print("\n" + "=" * 60)
    print("VECTOR DATABASE READY")
    print("=" * 60)


# ---------------------------------------------------
# CHAT LOOP
# ---------------------------------------------------

def start_chat():

    print("\n" + "=" * 60)
    print("LOADING VECTOR DATABASE")
    print("=" * 60)

    # ---------------------------------
    # Load Existing Index
    # ---------------------------------
    index, embedded_chunks = load_faiss_index()

    print("\n" + "=" * 60)
    print("HASANAH MART RAG CHAT")
    print("=" * 60)

    while True:

        # ---------------------------------
        # User Query
        # ---------------------------------
        query = input(
            "\nAsk your question "
            "(or type 'exit'): "
        )

        if query.lower() == "exit":
            break

        # ---------------------------------
        # Retrieve Chunks
        # ---------------------------------
        retrieved_results = retrieve_chunks(
            query=query,
            index=index,
            embedded_chunks=embedded_chunks,
            top_k=5
        )

        # ---------------------------------
        # Build Prompt
        # ---------------------------------
        prompt = build_prompt(
            query=query,
            retrieved_results=retrieved_results
        )

        # ---------------------------------
        # Generate Answer
        # ---------------------------------
        answer = generate_answer(prompt)

        # ---------------------------------
        # Display Retrieved Sources
        # ---------------------------------
        # print("\n" + "=" * 60)
        # print("RETRIEVED SOURCES")
        # print("=" * 60)

        # displayed_sources = set()

        # for result in retrieved_results:

        #     source = result["chunk"]["source"]

        #     if source not in displayed_sources:

        #         print(f"- {source}")

        #         displayed_sources.add(source)

        # ---------------------------------
        # Display Final Answer
        # ---------------------------------
        print("\n" + "=" * 60)
        print("ANSWER")
        print("=" * 60)

        print(answer)

        print("\n" + "=" * 60)


# ---------------------------------------------------
# MAIN MENU
# ---------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 60)
        print("HASANAH MART RAG SYSTEM")
        print("=" * 60)

        print("\n1. Build Vector Database")
        print("2. Start RAG Chat")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        # ---------------------------------
        # Build Vector Database
        # ---------------------------------
        if choice == "1":

            build_vector_database()

        # ---------------------------------
        # Start Chat
        # ---------------------------------
        elif choice == "2":

            start_chat()

        # ---------------------------------
        # Exit
        # ---------------------------------
        elif choice == "3":

            print("\nExiting system...")
            break

        else:

            print("\nInvalid choice.")


# ---------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------

if __name__ == "__main__":

    main()