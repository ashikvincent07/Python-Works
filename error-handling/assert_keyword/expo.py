def expo(base, pow):
    return base ** pow

assert expo(2, 3) == 8, "test case 1 failed with arg 2, 3"
assert expo(2, 2) == 4, "test case 2 failed with arg 2, 2"
assert expo(3, 3) == 27, "test case 3 failed with arg 3, 3"

print("OK")
