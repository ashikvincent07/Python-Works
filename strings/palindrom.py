def is_palindrom(word):

    word = word.casefold()

    return word == word[::-1]

print(is_palindrom("Malayalam"))