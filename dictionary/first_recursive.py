def first_recursive_character(word):

    wc = {}

    for ch in word:

        if ch in  wc.keys():
            return ch

        else:
            wc[ch] = 1

    return None

word = "malayalam"

print(first_recursive_character(word))