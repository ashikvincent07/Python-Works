class RemoveSpace:

    def solution(self, sentence):
        sentence_list = sentence.split()
        return " ".join(sentence_list)
    
remove_space_instance = RemoveSpace()

sentence = "India   is my      Country"

print(remove_space_instance.solution(sentence))
