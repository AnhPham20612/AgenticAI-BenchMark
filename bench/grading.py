import re

def found (answer, expected):
    """Return 1.0 if the answer names the expected version, else 0.0."""
    pattern = r"(?<![\d.])" + re.escape(expected) + r"(?![\d]|\.\d)"
    return re.search(pattern, answer) is not None

def grade_version(answer, newest, partial):
    if found(answer, newest):
        return 1.0
    for version in partial:
        if found(answer,version):
            return 0.5
    return 0
