from json import load

file_path = "json-works/student_data.json"

fr = open(file_path, "r", encoding= "utf-8")

data = load(fr) # convert json to python native type

# for st in data:
#     print(st.get("name"))

students_interested_in_photography = [st.get("name") for st in data if "Photography" in st.get("interests")]

# print("students_interested_in_photography : ",end="")
# for s in students_interested_in_photography:
#     print(s,end=", ")

# print()

full_time_students_name = [st.get("name") for st in data if st.get("is_full_time")]
print("full_time_students : ",end="")
for s in full_time_students_name:
    print(s,end=", ")