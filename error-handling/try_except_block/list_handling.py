# error handling
# sum, min, max, sort

lst = ["10", "20", "hello", "300", "hai", "4 00", "5"]

int_lst = []

for el in lst:
    try:
        int_lst.append(int(el))
    except Exception as e:
        print(e)

print(sum(int_lst))
print(max(int_lst))
print(min(int_lst))
print(sorted(int_lst))