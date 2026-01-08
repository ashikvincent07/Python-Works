from json import load

file_path = "json-works/jobs.json"

fr = open(file_path, "r", encoding= "utf-8")

data = load(fr)

role_with_it_operaions_skill = [j.get("role") for j in data if "IT Operations" in j.get("skills")]
print(role_with_it_operaions_skill)