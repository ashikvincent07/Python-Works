def consonants_count(word) :

    count = 0
     
    VOWELS = "aeiou"

    for ch in word.casefold():

        if ch not in VOWELS and ch.isalpha():
            count += 1

    return count

print(consonants_count("Hello12")) 
