words = ["cat", "act", "madam", "dam", "madam"]

palindrome_words = [w for w in words if w == w[::-1]]

recursive_palindrome_count = {}

for word in palindrome_words:

    if word in recursive_palindrome_count:
        recursive_palindrome_count[word] += 1

    else:
        recursive_palindrome_count[word] = 1

recursive_palindrome = {k for k, v in recursive_palindrome_count.items() if v > 1}

print(recursive_palindrome)