import os

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

print("Gemini API key found successfully")
print("AI Code Review script is ready")
