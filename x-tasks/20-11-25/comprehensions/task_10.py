text = "banana"

frequency = {char : text.count(char) for char in set(text)}

print(frequency)