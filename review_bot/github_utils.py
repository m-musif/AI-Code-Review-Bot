import requests


def read_pr_diff(file_path: str = "pr_diff.txt") -> str:
    with open(file_path, "r") as file:
        return file.read()


def save_review(review: str, file_path: str = "review.txt") -> None:
    with open(file_path, "w") as file:
        file.write(review)


def get_changed_files(github_token: str, repo_name: str, pr_number: str) -> list[dict]:
    url = f"https://api.github.com/repos/{repo_name}/pulls/{pr_number}/files"

    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()
