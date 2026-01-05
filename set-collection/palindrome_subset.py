str = "abcdcdbaabaa"

search_word = "ba"

search_len = len(search_word)

limit = len(str)

count = 0

for i in range(0, (limit-search_len)+1):
    if str[i:i+search_len] == search_word:
        count += 1

print(count)


