import json

json_file = "people.json"

with open(json_file, "r", encoding='utf-8') as f:
    people = json.load(f)

for person in people:
    print(f"Hello, {person['age']} year old {person['first_name']}")
