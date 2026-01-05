words = ["hello","hai","hello","is"]

r_index = -1
non_r_index = -1


recursive_word = [10]

non_recursive_word = [10]

for w in words :
    count = 0

    for d in words:

        if w == d :
            count += 1
        if count > 1:
            if w not in recursive_word:
                r_index += 1
                recursive_word[r_index] = w

    if count < 2:
        non_r_index += 1
        non_recursive_word[non_r_index] = w
                

            
 

print(f"Recursive words : {recursive_word}")
print(f"Non recursive word = {non_recursive_word}")