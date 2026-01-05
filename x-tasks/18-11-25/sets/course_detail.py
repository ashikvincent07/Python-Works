python_students = {"Alice", "Bob", "Charlie"}
ml_students = {"Bob", "David", "Eve"}

study_both_courses = python_students.intersection(ml_students)

only_python = python_students.difference(ml_students)

all_students = python_students.union(ml_students)

print(study_both_courses)

print(only_python)

print(all_students)