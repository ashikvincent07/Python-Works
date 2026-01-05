class EndsWithCheck:

    def solution(self, word):

        w = input("Enter a word: ")

        return word.endswith(w)
    
word = "Hello"

ends_with_instance = EndsWithCheck()

print(ends_with_instance.solution(word))