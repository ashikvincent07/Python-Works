all_users = {"sachin", "dravid", "laxman", "ganguly", "sreenath", "zaheer", "dhoni", "yuvi", "kaif"}

sachin_friends = {"dravid", "laxman", "ganguly"}

dhoni_friends = {"dravid", "laxman", "yuvi", "kaif"}


mutual_friends = sachin_friends.intersection(dhoni_friends)

print(mutual_friends)

suggestion = all_users.difference(sachin_friends)

suggestion.remove("sachin")

# print(suggestion)

