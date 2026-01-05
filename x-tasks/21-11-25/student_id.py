students = {
"101": {"name": "Rahul", "age": 14, "grade": "B"},
"102": {"name": "Anita", "age": 15, "grade": "A"}
}

for k, v in students.items():
    
    if k == "102":
        pass
        # print(v.get("name"))
        
# update rahul's grade

for v in students.values():

    if v.get("name") == "Rahul":
        v["grade"] = "A+"
        

# print(students)

students.update({"103" : {"name": "Vikram", "age": 16, "grade": "B+"}})

# print(students)

# id with names

for k, v in students.items():
    pass
    # print(f"{k} : {v.get("name")}")



