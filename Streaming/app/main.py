import os
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

# Get user input for the question
question = input("Enter your question: ")

stream = client.chat.completions.create(
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
    ],
    stream=True
)

# Stream the response and print it in real-time
print("AI: ", end="")

# Stream the response and print it in real-time
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)