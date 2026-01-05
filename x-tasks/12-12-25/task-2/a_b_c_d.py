"""
A B C D
A B C D
A B C D
A B C D
"""
text = "ABCD"

for r in range(4):
    for c in range(4):
        print(text[c],end=" ")
    print()