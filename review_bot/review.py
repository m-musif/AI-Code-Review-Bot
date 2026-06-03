import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Reply with: Hello from Gemini AI Code Review Bot")
    print(response.text)

except Exception as error:
    print("Gemini API call failed.")
    print("Reason:", error)
    print("Workflow is still working. Gemini quota/API issue needs to be fixed separately.")
