class OccuranceFind:

    def solution(self):

        word = input("Enter a word: ")

        char = input("Enter a character in the word: ")

        if char not in word:
            print("Char not found")
        else:
            print(f"First occurance : {word.find(char)}\nLast occurance : {word.rfind(char)}")

occurance_find_instance = OccuranceFind()

occurance_find_instance.solution()