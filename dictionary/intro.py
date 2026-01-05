# super_hero = {"name" : "batman", "universe" : "dc", "power" : "rich, tech, detective"}

# print(super_hero["name"])

# print(super_hero["power"])

employee = {"id" : 29468, "name" : "Ashik", "department" : "sales", "location" : "thrissur", "salary" : 20000}

# print(f"Name : {employee["name"]}")

employee["email"] = "ashik@gmail.com" # add new key value pair if key not exist else update the value of the key

# print(employee["email"])

employee["location"] = "guruvayoor"

# print(employee["location"])

if "email" in employee:
    print("exist")

else:
    print("not exist")