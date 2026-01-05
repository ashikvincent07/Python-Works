class AnagramCheck:

    def solution(self, w1, w2):

        if len(w1) != len(w2):
            return False
        
        if sorted(w1.casefold()) == sorted(w2.casefold()):
            return True
        
        return False
    
anagram_chk_instance = AnagramCheck()

print(anagram_chk_instance.solution("listen", "silenn"))
