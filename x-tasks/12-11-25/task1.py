words = ["hello","hai","hello","is"]

recursive_word = []

non_recursive_word = []

for w in words :

    if words.count(w) > 1:

        if w not in recursive_word:
            recursive_word.append(w)
            
    else:
        non_recursive_word.append(w)

print(f"Recursive words : {recursive_word}")
print(f"Non recursive word = {non_recursive_word}")