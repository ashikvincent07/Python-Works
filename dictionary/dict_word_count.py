words = ["hai", "hello", "hai", "hello", "python"]

dict_words = {}

# for w in set(words):
#     dict_words[w] = words.count(w)

for w in words:

    if w in dict_words:

        dict_words[w] += 1

    else:

        dict_words[w] = 1
    
    # if w not in dict_words:

    #     count = 0

    #     for c in words:
    #         if w == c:
    #             count += 1

    #     dict_words[w] = count

print(dict_words)

     