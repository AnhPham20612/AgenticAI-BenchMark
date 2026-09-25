from bench.grading import grade_version

test[
    ("The latest is Python 3.14.7.", "3.14.7"),
    ("The latest is v3.14.7.",       "3.14.7"),
    ("The latest is Python 3.14.71.", "3.14.7"),
    ("Version 13.14.7 is out.",      "3.14.7"),
]