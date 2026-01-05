text = "Python programming is very interesting"

result = [w for w in text.split() if len(w) > 5]

print(result)