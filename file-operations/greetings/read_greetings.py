file_path = "file-operations/greetings/greetings.txt"

fr = open(file_path, "r")

gt_set = {line.rstrip("\n") for line in fr}

print(gt_set)