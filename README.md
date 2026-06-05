# AI Code Review Bot

An AI-powered GitHub Pull Request review bot that automatically analyzes code changes, generates review feedback using an LLM, posts a detailed review summary on the Pull Request, and adds inline comments directly on changed lines.

---

## Features

* Automated GitHub Pull Request reviews
* AI-powered code analysis using Groq LLM
* GitHub Actions integration
* Review only changed files
* Supports multiple programming languages
* Pull Request summary comments
* Inline review comments on changed code
* File filtering and diff parsing
* Modular architecture for easy extension

---

## Architecture

```text
GitHub Pull Request
          │
          ▼
    GitHub Actions
          │
          ▼
      review.py
          │
    ┌─────┼─────────┐
    ▼     ▼         ▼
Diff   GitHub    Prompt
Parser   API    Builder
    │
    ▼
 Groq LLM
    │
    ▼
 AI Review
    │
 ┌──┴───────────┐
 ▼              ▼
PR Comment   Inline Comment
```

---

## Project Structure

```text
AI-Code-Review-Bot/
│
├── .github/
│   └── workflows/
│       └── ai-code-review.yml
│
├── review_bot/
│   ├── ai_reviewer.py
│   ├── config.py
│   ├── diff_parser.py
│   ├── github_utils.py
│   ├── prompts.py
│   ├── review.py
│   └── review_utils.py
│
├── screenshots/
│
├── requirements.txt
└── README.md
```

---

## How It Works

1. A Pull Request is opened.
2. GitHub Actions triggers automatically.
3. Changed files are collected using the GitHub API.
4. Diffs are filtered and parsed.
5. Groq LLM analyzes the changes.
6. A review summary is posted on the PR.
7. Inline comments are added to changed code.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/m-musif/AI-Code-Review-Bot.git
cd AI-Code-Review-Bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
GROQ_API_KEY=your_groq_api_key
```

---

## GitHub Secrets

Add these repository secrets:

```text
GITHUB_TOKEN
GROQ_API_KEY
```

---

## Example Review Output

```text
Severity: MEDIUM

Issue:
Missing error handling around API request.

Suggested Fix:
Wrap request in try/except and log failures.

Relevant Line:
get_pull_request()
```

---

## Screenshots

Add screenshots inside:

```text
screenshots/
```

Recommended screenshots:

* GitHub Actions Success
* Pull Request Review
* Inline Comments
* Merged Pull Request

---

## Technologies Used

* Python
* GitHub Actions
* GitHub API
* Groq LLM
* REST APIs
* CI/CD Automation

---

## Future Improvements

* Multi-model support
* Review severity scoring
* Code quality metrics
* Security-focused review mode
* Support for larger repositories

---

## Author

Muhammad Musif

GitHub:
https://github.com/m-musif

```
```
