from bench.grading import grade_version, grade_abstain
from bench.truth import get_truth

# ---------- 1. Ground truth ----------
newest, partial = get_truth("nodejs")
print("newest: ", newest)
print("partial:", partial)
print()

# ---------- 2. Version grader ----------
version_tests = [                                  # ← replace this whole block
    (f"Use Node {newest}",         1.0),
    (f"The LTS is {partial[0]}",   0.5),
    ("Node 18 is great",           0.0),
    (f"Try Node {newest}1",        0.0),
    ("Node 18.20.8 is the latest", 0.0),   # NEW
]

for answer, expected_score in version_tests:      # ← this loop stays the same
    score = grade_version(answer, newest, partial)
    result = "PASS" if score == expected_score else "FAIL"
    print(result, score, "<--", answer)
print()

# ---------- 3. Abstain grader ----------
abstain_tests = [
    ("I couldn't find any product called Quantavox Studio.", 1.0),
    ("Quantavox Studio does not exist as far as I know.",    1.0),
    ("The latest version of Quantavox Studio is 4.2.1.",     0.0),
]

for answer, expected_score in abstain_tests:
    score = grade_abstain(answer)
    result = "PASS" if score == expected_score else "FAIL"
    print(result, score, "<--", answer)