file_path = "C:/Development-Journey/Python-Works/file-operations/words/words.txt"

fr = open(file_path, "r")

palindrome = []

for line in fr:

    line = line.rstrip("\n")
    word = line.replace(" ", "")

    if word == word[::-1]:
        palindrome.append(word)

print(palindrome)