import yaml

with open("questions.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

for q in data["questions"]:
    print(q["id"], "->", q["question"])