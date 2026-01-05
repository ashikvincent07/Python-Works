company = {
"sales": {"manager": "Kiran", "team": {"T1": "Raj", "T2": "Neha"}},
"tech": {"manager": "Asha", "team": {"T1": "Dev", "T2": "Sonia"}}
}


# Print the name of "T2" in the "tech" department.

for k, v in company.items():

    if k == "tech":
        pass
        # print(v["team"]["T2"])


# print all the team member IDs (T1, T2) of "sales"

for k, v in company.items():

    if k == "sales":
        print(v["team"])
        pass