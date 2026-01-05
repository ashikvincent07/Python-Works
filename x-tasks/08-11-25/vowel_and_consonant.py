def display_vowel_and_cosonant_count(word):

    vowel_count = 0
    consonant_count = 0

    VOWELS = "aeiou"

    for ch in word.casefold():

        if ch in VOWELS:
            vowel_count += 1

        elif ch not in VOWELS and ch.isalpha():
            consonant_count += 1

    print(f"Vowel count = {vowel_count}")
    print(f"Consonant count = {consonant_count}")

display_vowel_and_cosonant_count("Hello therE")