# rag/prompt_builder.py


def build_prompt(query,
                 retrieved_results,
                 max_context_chars=4000):
    """
    Build final RAG prompt using:
    - user query
    - retrieved chunks
    """

    # ---------------------------------
    # Collect Context Chunks
    # ---------------------------------
    context_parts = []

    current_length = 0

    for result in retrieved_results:

        chunk = result["chunk"]

        chunk_text = chunk["content"]

        # Stop if context becomes too large
        if (
            current_length + len(chunk_text)
            > max_context_chars
        ):
            break

        context_parts.append(
            f"Source: {chunk['source']}\n"
            f"{chunk_text}"
        )

        current_length += len(chunk_text)

    # Join all context chunks
    context = "\n\n" + ("-" * 50) + "\n\n".join(
        context_parts
    )

    # ---------------------------------
    # Final Prompt
    # ---------------------------------
    prompt = f"""
You are an AI assistant for Hasanah Mart.

Your task is to answer customer questions
using ONLY the provided context.

If the answer is not found in the context,
say:
"I could not find sufficient information."

Do not make up information.

==============================
CONTEXT
==============================

{context}

==============================
QUESTION
==============================

{query}

==============================
ANSWER
==============================
"""

    return prompt