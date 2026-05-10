# rag/generator.py

from openai import OpenAI
from dotenv import load_dotenv
import os

from rag.vector_store import load_faiss_index
from rag.retriever import retrieve_chunks
from rag.prompt_builder import build_prompt
from api.core.config import settings

# ---------------------------------
# Load Environment Variables
# ---------------------------------
load_dotenv()

# ---------------------------------
# Initialize OpenAI Client
# ---------------------------------
client = OpenAI(
    api_key=settings.openai_api_key
)

# ---------------------------------
# Chat Model
# ---------------------------------
CHAT_MODEL = settings.chat_model


def generate_answer(prompt,
                    temperature=settings.temperature):
    """
    Generate answer from OpenAI model.
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,

        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant "
                    "for Hasanah Mart."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=temperature
    )

    answer = response.choices[0].message.content

    return answer