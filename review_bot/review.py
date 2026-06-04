import os

from review_bot.ai_reviewer import generate_ai_review
from review_bot.github_utils import read_pr_diff, save_review
from review_bot.prompts import CODE_REVIEW_PROMPT

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")

pr_diff = read_pr_diff()
prompt = CODE_REVIEW_PROMPT.format(pr_diff=pr_diff)

try:
    review = generate_ai_review(api_key, prompt)

    print("\n===== AI CODE REVIEW =====\n")
    print(review)

    save_review(review)

except Exception as error:
    print("AI review generation failed.")
    print(error)
