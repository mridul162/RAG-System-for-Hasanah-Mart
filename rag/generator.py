# rag/generator.py

from openai import OpenAI
from dotenv import load_dotenv
import os

from rag.vector_store import load_faiss_index
from rag.retriever import retrieve_chunks
from rag.prompt_builder import build_prompt

# ---------------------------------
# Load Environment Variables
# ---------------------------------
load_dotenv()

# ---------------------------------
# Initialize OpenAI Client
# ---------------------------------
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ---------------------------------
# Chat Model
# ---------------------------------
CHAT_MODEL = "gpt-4.1-mini"


def generate_answer(prompt,
                    temperature=0.2):
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