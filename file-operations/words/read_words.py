file_path = "C:/Development-Journey/Python-Works/file-operations/words/words.txt"

fr = open(file_path, "r")

result = []

for line in fr:
    
    line = line.rstrip("\n")
    word = line.replace(" ", "")
    result.append(word)

print(result)