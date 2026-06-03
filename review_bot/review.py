import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

try:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Reply with: Hello from Gemini AI Code Review Bot"
    )

    print(response.text)

except Exception as error:
    print("Gemini API call failed.")
    print("Reason:", error)
    print("Workflow is still working. Gemini quota/API issue needs to be fixed separately.")
