words = ["proffesional", "cat", "acting", "programming", "dam", "process", "proffesional"]

starts_with_str = {word for word in words if word.startswith("pro")}

print(starts_with_str)

ends_with_str = {word for word in words if word.endswith("ing")}

print(ends_with_str)