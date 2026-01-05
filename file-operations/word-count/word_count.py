story_path = "C:\\Development-Journey\\Python-Works\\file-operations\\word-count\\story.txt"

fr_story = open(story_path, "r")

wc = {}

for line in fr_story:

    line = line.rstrip("\n")

    words = line.split(" ")

    for w in words:

        w=w.rstrip(",")
        w=w.rstrip(".")

        if w in wc:
            wc[w] += 1

        else:
            wc[w] = 1

print(wc)

max_word_count = {k : v for k,v in wc.items() if v == max(wc.values()) and k.isalpha()}

print(f"Max count = {max_word_count}")



    



