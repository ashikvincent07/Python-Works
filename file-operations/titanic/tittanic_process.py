file_path = "file-operations/titanic/dataset.csv"

fr = open(file_path, "r")

import csv

reader = csv.DictReader(fr)

data = [row for row in reader]

# print(data[1])


for row in data:
    for k in row.keys():
        if k == "Name":
            pass
#           print(row.get(k))

male_count = 0

for row in data:
    for v in row.values():
        if v == "male":
            male_count += 1
# print(male_count)

genders = [info.get("Sex") for info in data]
male_count = genders.count("male")
female_count = genders.count("female")

# print(f"Male count = {male_count}")
# print(f"Female count = {female_count}")

survived_list = [info.get("Survived") for info in data]
survived_count = survived_list.count("1")
not_survived_count = survived_list.count("0")

# print(f"Survived count = {survived_count}")
# print(f"Not survived count = {not_survived_count}")

age_list = [int(info.get("Age")) for info in data if info.get("Age").isdigit()]
old = max(age_list)
young = min(age_list)
old_list = [info.get("Name") for info in data  if info.get("Age") == str(old)]
young_list = [info.get("Name") for info in data if info.get("Age") == str(young)]
# print(f"Oldest : {old_list}")
# print(f"Youngest : {young_list}")


first_ten = data[:10]
first_ten_names = [s.get("Name") for s in first_ten]
# print(first_ten_names)



all_boarding_station = [s.get("Embarked") for s in data]
boarding_station_count = {e : all_boarding_station.count(e) for e in all_boarding_station if e != ""} 
# print(boarding_station_count)



children_list_lt_age_10 = [s for s in data if s.get("Age").isdigit() and int(s.get("Age")) < 10]
children_list_lt_age_10_survived = [s for s in children_list_lt_age_10 if s.get("Survived") == "1"] 

total_children_lt_age_10 = len(children_list_lt_age_10)
total_survived_lt_age_10_survived = len(children_list_lt_age_10_survived)

# print(f"Total children below age 10: {total_children_lt_age_10}")
# print(f"Total survived children below age 10 : {total_survived_lt_age_10_survived}")

survived_list = [s.get("Survived") for s in data]
total_survived = survived_list.count("1")
total_passenger = len(survived_list)

survived_percentage = round(total_survived / total_passenger * 100, 2)
# print(f"Survival rate = {survived_percentage}")





#survival rate gender wise
male_list = [s for s in data if s.get("Sex") == "male"]
male_survived_list = [s for s in male_list if s.get("Survived") == "1"]

female_list = [s for s in data if s.get("Sex") == "female"]
female_survived_list = [s for s in female_list if s.get("Survived") == "1"]

male_survival_rate = round((len(male_survived_list))/(len(male_list)) * 100, 2)
# print(f"male_survival_rate = {male_survival_rate}")

female_survival_rate = round((len(female_survived_list))/(len(female_list)) * 100, 2)
# print(f"female_survival_rate = {female_survival_rate}")





#class wise survival rate
class_wise_passenger = [s.get("Pclass") for s in data]
class_wise_passenger_count = {s : class_wise_passenger.count(s) for s in class_wise_passenger}
class_wise_survived = [s.get("Pclass") for s in data if s.get("Survived") == "1"]
class_wise_survived_count = {s : class_wise_survived.count(s) for s in class_wise_survived}

print(f"First class survival rate = {round(class_wise_survived_count.get("1") / class_wise_passenger_count.get("1") * 100, 2)}")
print(f"Second class survival rate = {round(class_wise_survived_count.get("2") / class_wise_passenger_count.get("2") * 100, 2)}")
print(f"Third class survival rate = {round(class_wise_survived_count.get("3") / class_wise_passenger_count.get("3") * 100, 2)}")



