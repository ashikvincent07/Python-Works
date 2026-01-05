class WordFreq:

    def solution(self):

        sentence = "They promised once and for all, but once and for all meant nothing"

        search = input("Enter a word to search: ")

        print(f"Total occurance : {sentence.count(search)}")


word_freq_instance = WordFreq()

word_freq_instance.solution()