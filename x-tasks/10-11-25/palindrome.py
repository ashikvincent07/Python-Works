def is_palindrome(word) :

    return word.casefold() == word.casefold()[::-1]

print(is_palindrome("malayalam"))