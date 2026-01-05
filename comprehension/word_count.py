words = ["am", "in", "on", "off", "in", "out", "off"]

word_count = {word : words.count(word) for word in set(words)}

print(word_count)