team = {
"player1": {"name": "Rohit", "role": "Batsman"},
"player2": {"name": "Bumrah", "role": "Bowler"}
}

# role of bumrah

# print("Role of Bumrah : ",end="")

for v in team.values():

    if v.get("name") == "Bumrah":
        pass
        # print(v.get("role"))


# add a new key "matches" for "Rohit" with value 250.

for v in team.values():

    if v.get("name") == "Rohit":
        pass
        # v["matches"] = 250
        # print(v)

# remove the "role" of "Bumrah"

for v in team.values():

    if v.get("name") == "Bumrah":
        # v.pop("role")
        # print(v)
        pass



