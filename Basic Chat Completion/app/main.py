import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize the Groq client with the API key
client = Groq(api_key=api_key)

question = input("Enter your question: ")

# Use the Groq client to get an answer to the question
answer = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "You are a personal assistant to help the user with their queries."
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print("Answer: object", answer.model_dump())
print("Answer:", answer.choices[0].message.content)