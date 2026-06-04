def read_pr_diff(file_path: str = "pr_diff.txt") -> str:
    with open(file_path, "r") as file:
        return file.read()


def save_review(review: str, file_path: str = "review.txt") -> None:
    with open(file_path, "w") as file:
        file.write(review)
