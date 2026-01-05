words = ["housefull", "peaceful", "beautiful", "harmful", "powerful", "thinkful"]

ends_with_ful = [w.endswith("ful") for w in words]
is_all_ends_with_ful = all(ends_with_ful)
# print(is_all_ends_with_ful)


words2 = ["program", "apple", "python", "property"]
starts_with_pro = [w.startswith("pro") for w in words2]
print(any(starts_with_pro))