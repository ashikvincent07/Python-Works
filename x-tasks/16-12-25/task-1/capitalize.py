class CapitalizeEachWord:

    def solution(self, sentence):
        return sentence.title()
    
capitalize_each_word_instance = CapitalizeEachWord()

sentence = "India is my country"

print(capitalize_each_word_instance.solution(sentence))