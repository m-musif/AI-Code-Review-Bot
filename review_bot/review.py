import os

from review_bot.ai_reviewer import generate_ai_review
from review_bot.diff_parser import split_diff_by_file
from review_bot.github_utils import read_pr_diff, save_review
from review_bot.prompts import FILE_REVIEW_PROMPT

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")

pr_diff = read_pr_diff()
changed_files = split_diff_by_file(pr_diff)

if not changed_files:
    message = "No reviewable files found in this pull request."
    print(message)
    save_review(message)
    exit(0)

all_reviews = []

try:
    for changed_file in changed_files:
        file_name = changed_file["file_name"]
        file_diff = changed_file["file_diff"]

        prompt = FILE_REVIEW_PROMPT.format(
            file_name=file_name,
            file_diff=file_diff
        )

        print(f"\n===== REVIEWING FILE: {file_name} =====\n")

        file_review = generate_ai_review(api_key, prompt)

        all_reviews.append(
            f"## File: `{file_name}`\n\n{file_review}"
        )

    final_review = "\n\n---\n\n".join(all_reviews)

    print("\n===== AI CODE REVIEW =====\n")
    print(final_review)

    save_review(final_review)

except Exception as error:
    print("AI review generation failed.")
    print(error)
