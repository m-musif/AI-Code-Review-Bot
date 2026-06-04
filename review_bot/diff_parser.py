IGNORED_FILE_PATTERNS = [
    ".gitkeep",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "node_modules/",
    "dist/",
    "build/",
    ".env",
]


def should_review_file(file_name: str) -> bool:
    for pattern in IGNORED_FILE_PATTERNS:
        if pattern in file_name:
            return False

    return True


def split_diff_by_file(pr_diff: str) -> list[dict[str, str]]:
    files = []
    current_file = None
    current_diff_lines = []

    for line in pr_diff.splitlines():
        if line.startswith("diff --git"):
            if current_file and current_diff_lines and should_review_file(current_file):
                files.append({
                    "file_name": current_file,
                    "file_diff": "\n".join(current_diff_lines)
                })

            parts = line.split(" ")
            current_file = parts[-1].replace("b/", "")
            current_diff_lines = [line]
        else:
            if current_file:
                current_diff_lines.append(line)

    if current_file and current_diff_lines and should_review_file(current_file):
        files.append({
            "file_name": current_file,
            "file_diff": "\n".join(current_diff_lines)
        })

    return files
