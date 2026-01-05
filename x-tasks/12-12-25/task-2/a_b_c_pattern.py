"""
A B C D
B C D A
C D A B
D A B C
"""
text = "ABCD"

for r in range(4):
    for c in range(4):
        print(text[(r + c) % 4], end=" ")
    print()
