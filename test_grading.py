from bench.grading import grade_version, grade_abstain
from bench.truth import get_truth

# ---------- 1. Ground truth ----------
newest, partial = get_truth("nodejs")
print("newest: ", newest)
print("partial:", partial)
print()

# ---------- 2. Version grader ----------
# Uses the REAL Node.js versions fetched above, so the tests stay correct
# even when a new Node.js version comes out.
version_tests = [
    (f"Use Node {newest}",       1.0),   # newest version       -> full credit
    (f"The LTS is {partial[0]}", 0.5),   # older maintained line -> half credit
    ("Node 18 is great",         0.0),   # old, unsupported     -> wrong
    (f"Try Node {newest}1",      0.0),   # extra digit stuck on -> wrong
]

for answer, expected_score in version_tests:
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