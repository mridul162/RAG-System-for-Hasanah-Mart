# api/services/rag_service.py

from rag.vector_store import load_faiss_index
from rag.retriever import retrieve_chunks
from rag.prompt_builder import build_prompt
from rag.generator import generate_answer
from api.core.logging import get_logger
import time
import dotenv
dotenv.load_dotenv()

logger = get_logger(__name__)


class RAGService:

    def __init__(self):

        logger.info("Loading FAISS index...")

        self.index, self.embedded_chunks = (
            load_faiss_index()
        )

        logger.info("FAISS index loaded successfully!")

    # -------------------------------------------------
    # Main RAG Pipeline
    # -------------------------------------------------

    def ask(
        self,
        query: str,
        top_k: int = 5,
        include_sources: bool = True
    ):

        logger.info(
            f"Received query: {query}"
        )

        total_start_time = time.perf_counter()

        try:

            # -----------------------------------------
            # Retrieve Relevant Chunks
            # -----------------------------------------
            logger.info(
                "Retrieving relevant chunks..."
            )

            retrieval_start = time.perf_counter()

            retrieved_results = retrieve_chunks(
                query=query,
                index=self.index,
                embedded_chunks=self.embedded_chunks,
                top_k=top_k
            )

            logger.info(
                f"Retrieved "
                f"{len(retrieved_results)} chunks."
            )

            retrieval_time = (
                time.perf_counter() - retrieval_start
            )

            logger.info(
                f"Retrieval completed in "
                f"{retrieval_time:.3f} seconds."
            )
                        

            # -----------------------------------------
            # Build Prompt
            # -----------------------------------------
            logger.info(
                "Building RAG prompt..."
            )

            prompt_start = time.perf_counter()

            prompt = build_prompt(
                query=query,
                retrieved_results=retrieved_results
            )

            prompt_time = (
                time.perf_counter() - prompt_start
            )

            logger.info(
                f"Prompt built in {prompt_time:.3f} seconds."
            )

            # -----------------------------------------
            # Generate Final Answer
            # -----------------------------------------
            logger.info(
                "Generating final answer..."
            )

            generation_start = time.perf_counter()

            answer = generate_answer(
                prompt=prompt
            )

            logger.info(
                "Answer generated successfully."
            )

            generation_time = (
                time.perf_counter() - generation_start
            )

            logger.info(
                f"Answer generated in "
                f"{generation_time:.3f} seconds."
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

            logger.info(
                "Returning RAG response."
            )

            total_time = time.perf_counter() - total_start_time

            logger.info(
                f"Total RAG pipeline completed in {total_time:.3f} seconds."
            )

            return response

        except Exception:

            logger.exception(
                "Error occurred inside RAG pipeline."
            )

            raise