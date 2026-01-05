class WordCheck:

    def solution(self, word):
        string = "India is my country."
        return word.casefold() in string.casefold()
    

word_chk_instance_1 = WordCheck()

print(word_chk_instance_1.solution("hi"))

