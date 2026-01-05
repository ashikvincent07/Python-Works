classroom = {
"student1": {"name": "John", "age": 15},
"student2": {"name": "Mary", "age": 16}
}


student_info = classroom.values()

for info in student_info :
    if info.get("name") == "Mary":
        print(f"Age of {info.get("name")} {info.get("age")}")