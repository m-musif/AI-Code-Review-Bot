CODE_REVIEW_PROMPT = """
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


FILE_REVIEW_PROMPT = """
You are a senior software engineer reviewing a single changed file in a GitHub Pull Request.

File name:
{file_name}

File diff:
{file_diff}

Provide a concise review with:
1. Bugs
2. Security issues
3. Code quality issues
4. Suggestions
"""
