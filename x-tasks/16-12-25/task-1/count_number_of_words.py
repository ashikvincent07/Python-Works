class CountWordNumber:

    def solution(self, sentence):
        sentence = sentence.strip()
        total_words = len(sentence.split())

        return total_words
    

count_words = CountWordNumber()

sentence = "India is  my country"

print(count_words.solution(sentence))