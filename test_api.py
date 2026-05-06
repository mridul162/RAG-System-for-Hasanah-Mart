from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

print(os.getenv("OPENAI_API_KEY"))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Hello world"
)

print(len(response.data[0].embedding))