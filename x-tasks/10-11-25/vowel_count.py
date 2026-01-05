def count_vowels(word):
    count = 0

    VOWELS = "aeiou"

    for ch in word.casefold():

        if ch in VOWELS:
            count += 1

    return count

print(count_vowels("Hello"))