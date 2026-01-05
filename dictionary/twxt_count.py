text = "helloworld"

tc = {}

for ch in text:

    if ch in tc:
        tc[ch] += 1

    else:
        tc[ch] = 1

print(tc)