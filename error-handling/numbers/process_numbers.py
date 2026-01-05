file_path = "error-handling/numbers/numbers.txt"

numbers = []

try :
    fr = open(file_path, "r")  
    for line in fr:
        line = line.rstrip("\n")
        try :
            numbers.append(int(line))
        except Exception as e:
            continue


    max_val = max(numbers)
    min_val = min(numbers)
    total = sum(numbers)
    frequency = {num : numbers.count(num) for num in set(numbers)}
    max_frequency_num = [n for n,c in frequency.items() if c == max(frequency.values())]

    print(f"Max = {max_val}")
    print(f"Min = {min_val}")
    print(f"Sum = {total}")
    print(f"Most frequent num = {max_frequency_num}")
  

except Exception as e:
    print(e)

