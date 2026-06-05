from review_bot.ai_reviewer import generate_ai_review
from review_bot.config import (
    GITHUB_TOKEN,
    GROQ_API_KEY,
    MAX_FILES_TO_REVIEW,
    PR_NUMBER,
    REPO_NAME,
)
from review_bot.diff_parser import get_first_changed_line, should_review_file
from review_bot.github_utils import (
    get_changed_files,
    get_pull_request,
    post_inline_comment,
    save_review,
)
from review_bot.prompts import FILE_REVIEW_PROMPT

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing")

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN is missing")

changed_files = get_changed_files(GITHUB_TOKEN, REPO_NAME, PR_NUMBER)

pull_request = get_pull_request(GITHUB_TOKEN, REPO_NAME, PR_NUMBER)
commit_id = pull_request["head"]["sha"]

print(f"PR Head Commit: {commit_id}")

reviewable_files = [
    file for file in changed_files
    if should_review_file(file["filename"]) and file.get("patch")
]

reviewable_files = reviewable_files[:MAX_FILES_TO_REVIEW]

if not reviewable_files:
    message = "No reviewable files found in this pull request."
    print(message)
    save_review(message)
    exit(0)

all_reviews = []

try:
    for changed_file in reviewable_files:
        file_name = changed_file["filename"]
        file_diff = changed_file["patch"]
        line_number = get_first_changed_line(file_diff)

        prompt = FILE_REVIEW_PROMPT.format(
            file_name=file_name,
            file_diff=file_diff
        )

        print(f"\n===== REVIEWING FILE: {file_name} =====\n")

        file_review = generate_ai_review(GROQ_API_KEY, prompt)

        all_reviews.append(
            f"## File: `{file_name}`\n\n{file_review}"
        )

        if line_number:
            try:
                post_inline_comment(
                    github_token=GITHUB_TOKEN,
                    repo_name=REPO_NAME,
                    pr_number=PR_NUMBER,
                    commit_id=commit_id,
                    file_path=file_name,
                    line_number=line_number,
                    body=(
                        f"🤖 AI review generated for `{file_name}`.\n\n"
                        "See full PR comment for details."
                    )
                )
                print(f"Inline comment posted for {file_name} on line {line_number}")
            except Exception as inline_error:
                print(f"Inline comment failed for {file_name}: {inline_error}")

    summary = f"Reviewed {len(reviewable_files)} file(s)."

    final_review = (
        summary
        + "\n\n---\n\n"
        + "\n\n---\n\n".join(all_reviews)
    )

    print("\n===== AI CODE REVIEW =====\n")
    print(final_review)

    save_review(final_review)

except Exception as error:
    print("AI review generation failed.")
    print(error)
