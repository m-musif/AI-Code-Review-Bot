import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")

client = Groq(api_key=api_key)

with open("pr_diff.txt", "r") as file:
    pr_diff = file.read()

prompt = f"""
You are a senior software engineer.

Review the following GitHub Pull Request diff.

Provide:
1. Bugs
2. Security issues
3. Code quality issues
4. Suggestions

PR Diff:

{pr_diff}
"""

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    review = response.choices[0].message.content

    print("\n===== AI CODE REVIEW =====\n")
    print(review)

    with open("review.txt", "w") as file:
        file.write(review)

except Exception as error:
    print("Groq API call failed.")
    print(error)
