words = ["cat", "act", "madam", "dam", "malayalam"]

palindrome_words = {w for w in words if w == w[::-1]}

print(palindrome_words)