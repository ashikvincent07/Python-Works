def is_anagram_check(word_1, word_2):

    is_anagram = True

    if len(word_1) != len(word_2):
        return False

    for ch in word_1:

        ch_count_w1 = word_1.count(ch)

        ch_count_w2 = word_2.count(ch)

        if ch_count_w1 != ch_count_w2:

            is_anagram = False

            break

    return is_anagram


print(is_anagram_check("Cat".casefold(), "acT".casefold()))