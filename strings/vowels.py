def vowel_count(word):

    count = 0

    for ch in word:

        if ch in "aeiouAEIOU":
            count += 1

    return count

print(vowel_count("hello"))
