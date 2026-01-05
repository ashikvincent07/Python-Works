nums = [1, 2, 2, 3, 4, 4, 5]

seen = set()
duplicates = set()

for n in nums:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

only_once = set(nums) - duplicates
print(only_once)
