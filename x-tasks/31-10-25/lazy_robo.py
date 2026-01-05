limit = 10

sleeping_text = "(Robot sleeping....)"

i = 1

while i <= limit :
    if i == 7:
        print(sleeping_text,end=" ")
        i += 1
        continue
    print(i,end=" ")
    i += 1
