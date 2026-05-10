# api/services/rag_service.py

from rag.vector_store import load_faiss_index
from rag.retriever import retrieve_chunks
from rag.prompt_builder import build_prompt
from rag.generator import generate_answer


class RAGService:

    def __init__(self):

        print("\nLoading FAISS index...")

        self.index, self.embedded_chunks = (
            load_faiss_index()
        )

        print("FAISS index loaded successfully!")

    # -------------------------------------------------
    # Main RAG Pipeline
    # -------------------------------------------------

    def ask(self,
            query: str,
            top_k: int = 5,
            include_sources: bool = True):

        # -----------------------------------------
        # Retrieve Relevant Chunks
        # -----------------------------------------
        retrieved_results = retrieve_chunks(
            query=query,
            index=self.index,
            embedded_chunks=self.embedded_chunks,
            top_k=top_k
        )

        # -----------------------------------------
        # Build Prompt
        # -----------------------------------------
        prompt = build_prompt(
            query=query,
            retrieved_results=retrieved_results
        )

        # -----------------------------------------
        # Generate Final Answer
        # -----------------------------------------
        answer = generate_answer(
            prompt=prompt
        )

        # -----------------------------------------
        # Format Sources
        # -----------------------------------------
        sources = []

        if include_sources:

            for result in retrieved_results:

                chunk = result["chunk"]

                sources.append({
                    "source": chunk["source"],
                    "chunk_id": chunk["chunk_id"],
                    "distance": result["distance"],
                    "preview": chunk["content"][:300]
                })

        # -----------------------------------------
        # Final Response
        # -----------------------------------------
        response = {
            "query": query,
            "answer": answer,
            "sources": sources
        }

        return response