import re

def grade_version (answer, expected):
    """Return 1.0 if the answer names the expected version, else 0.0."""
    pattern = r"(?<![\d.])" + re.escape(expected) + r"(?![\d]|\.\d)"
    if re.search(pattern,answer):
        return 1.0
    return 0
