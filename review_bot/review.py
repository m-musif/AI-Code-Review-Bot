import os

from review_bot.ai_reviewer import generate_ai_review

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")

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
    review = generate_ai_review(api_key, prompt)

    print("\n===== AI CODE REVIEW =====\n")
    print(review)

    with open("review.txt", "w") as file:
        file.write(review)

except Exception as error:
    print("AI review generation failed.")
    print(error)
