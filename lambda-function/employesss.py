employees = [
    ["ashik", 30000, 1],
    ["sarath", 25000, 2],
    ["arun", 35000, 7],
    ["amal", 15000, 3]
]

print(employees)

print(sorted(employees))

sort_emp_sal = sorted(employees, key = lambda emp: emp[1])
print(sort_emp_sal)

sort_emp_exp = sorted(employees, key = lambda emp: emp[2])
print(sort_emp_exp)