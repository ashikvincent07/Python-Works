def is_pangram(sentence):

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    for ch in ALPHABET:

        if ch not in sentence.casefold():
            return False
        
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog"))