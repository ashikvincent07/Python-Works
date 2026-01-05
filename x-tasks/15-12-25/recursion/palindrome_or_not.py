word = input("Enter a word: ")

def palindrome_chk(w):
    if len(w) <= 1:         
        return True
    if w[0] != w[-1]:        
        return False
    return palindrome_chk(w[1:-1])  

print(palindrome_chk(word))
