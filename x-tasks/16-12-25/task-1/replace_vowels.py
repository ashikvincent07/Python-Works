class ReplaceVowels:

    def solution(self, word):
        VOWELS = "aeiou"

        for ch in word:
            if ch.casefold() in VOWELS:
                word = word.replace(ch, "*")

        return word
    
replace_word_instance = ReplaceVowels()

word = "Elephant"

print(replace_word_instance.solution(word))

