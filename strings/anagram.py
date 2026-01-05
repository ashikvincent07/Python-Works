def is_anagram(word1, word2):

    sort_w1 = sorted(word1.casefold())

    sort_w2 = sorted(word2.casefold())

    return sort_w1 == sort_w2

print(is_anagram("acT", "cat"))

print(is_anagram("car", "Arc"))