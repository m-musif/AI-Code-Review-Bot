FILE_REVIEW_PROMPT = """
You are a senior software engineer reviewing a single changed file in a GitHub Pull Request.

File name:
{file_name}

File diff:
{file_diff}

For every issue found, assign one severity:

🔴 HIGH
🟡 MEDIUM
🟢 LOW

For every issue, include:
- Severity
- Issue
- Suggested fix
- Relevant line or code area if visible in the diff

Review format:

## Bugs

## Security Issues

## Code Quality Issues

## Suggestions

Keep the review concise and actionable.
"""
