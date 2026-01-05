file_path = "C:/Development-Journey/Python-Works/file-operations/products.txt"

fr = open(file_path, "r")

for line in fr:
    print(line,end="")