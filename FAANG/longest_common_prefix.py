class Prefix:
    def solution(self, words):
        if not words:
            return ""

        prefix = words[0]

        for word in words[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
    
prefix_instance = Prefix()

words = ["international", "interstate", "interview", "internet", "ain"]

print(prefix_instance.solution(words))
