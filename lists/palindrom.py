def palindrome_words(words):

    palindrome = []

    for w in words:

        if w == w[::-1]:
            palindrome.append(w)
    
    return palindrome



words = ["cat", "act", "dam", "mad", "malayalam", "madam"]

print(palindrome_words(words))





