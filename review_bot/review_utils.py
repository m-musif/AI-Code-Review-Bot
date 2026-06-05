def extract_inline_comment(review: str) -> str:
    marker = "INLINE_COMMENT:"

    if marker not in review:
        return "AI review generated."

    return review.split(marker, 1)[1].strip()
