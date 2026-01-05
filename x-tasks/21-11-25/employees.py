employees = {
"E01": {"name": "Arjun", "dept": "HR"},
"E02": {"name": "Sara", "dept": "IT"},
"E03": {"name": "Manoj", "dept": "Finance"}
}


for v in employees.values():

    if v.get("name") == "Sara":
        pass
        # print(v.get("dept"))


# "Arjun"’s department from "HR" to "Admin"
for v in employees.values():

    if v.get("name") == "Arjun":
        v["dept"] = "Admin"

# print(employees)

# E04 -> name: "Lakshmi", dept: "Marketing"

employees.update({"E04" : {"name": "Lakshmi", "dept": "Marketing"}})

# print(employees)

# Loop through the dictionary and print employee IDs with their names.

for k, v in employees.items():
    pass
    # print(f"{k} : {v.get("name")}")

total_emp = len(employees)
print(total_emp)




