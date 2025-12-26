from dotenv import load_dotenv
import os

load_dotenv()

# Safe checks (do NOT print secrets)
print("AZURE_OPENAI_ENDPOINT set:", bool(os.getenv("AZURE_OPENAI_ENDPOINT")))
print("AZURE_OPENAI_API_KEY set:", bool(os.getenv("AZURE_OPENAI_API_KEY")))
