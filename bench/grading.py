def grade_version (answer, expected):
    """Return 1.0 if the answer names the expected version, else 0.0."""
    if expected in answer:
        return 1.0
    return 0
