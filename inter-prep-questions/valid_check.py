class StringCheck:

    def solution(self, string):
        stack = []
        dictionary = {"(":")", "{":"}", "[":"]", "<":">"}
        for s in string:
            if s in dictionary:
                stack.append(s)
            elif s in dictionary.values():
                if not stack:
                    return False
                last = stack.pop()

                if dictionary[last] != s:
                    return False

        return len(stack) == 0



string_check = StringCheck()
string = ""
print(string_check.solution(string))