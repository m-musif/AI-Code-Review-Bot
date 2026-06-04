def split_diff_by_file(pr_diff: str) -> list[dict[str, str]]:
    files = []
    current_file = None
    current_diff_lines = []

    for line in pr_diff.splitlines():
        if line.startswith("diff --git"):
            if current_file and current_diff_lines:
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

    if current_file and current_diff_lines:
        files.append({
            "file_name": current_file,
            "file_diff": "\n".join(current_diff_lines)
        })

    return files
