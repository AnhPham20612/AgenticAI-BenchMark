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


ABSTAIN_PHRASES = [
    "does not exist", "doesn't exist", "couldn't find", "could not find",
    "can't find", "cannot find", "no information", "not aware of",
    "unable to find", "no record", "not a known", "no reliable",
]


def grade_abstain(answer):
    """1.0 if the AI admits it can't find the (made-up) product, else 0.0."""
    text = answer.lower()
    for phrase in ABSTAIN_PHRASES:
            if phrase in text:
                 return 1.0
    return 0.0