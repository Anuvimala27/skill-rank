import json

with open('ex5.json', 'r') as file:
    example = json.load(file)

for i in example:
    if i.get("name") == "Old Fashioned" and i.get("type") == "donut":
        i["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break

with open('ex5.json', 'w') as file:
    json.dump(example, file, indent=2)
