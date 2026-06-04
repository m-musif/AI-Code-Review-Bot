import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")

client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Reply with: Hello from Groq AI Code Review Bot"}]
    )
    print(response.choices[0].message.content)

except Exception as error:
    print("Groq API call failed.")
    print("Reason:", error)
