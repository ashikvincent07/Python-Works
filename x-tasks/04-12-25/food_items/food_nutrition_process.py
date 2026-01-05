file_path = "x-tasks/04-12-25/food_items/Food_Nutrition_Dataset.csv"

import csv

fr = open(file_path, "r") 
reader = csv.DictReader(fr)
data = list(reader)
fr.close()

# total foods 
total_foods = len(data)
# print(f"Total foods : {total_foods}")


# which category has more food
all_category_list = [food.get("category") for food in data]
category_wise_food_count = {category : all_category_list.count(category) for category in set(all_category_list)}
max_food_count = max(category_wise_food_count.values())
category_with_most_food_count = [cat for cat,count in category_wise_food_count.items() if count == max_food_count]
# print(f"category_with_most_food_count : {category_with_most_food_count}")



# foods with high protien
highest_protien = max(float(food.get("protein")) for food in data)
high_protien_foods = [food.get("food_name") for food in data if float(food.get("protein")) == highest_protien]
# print(f"high_protien_foods : {high_protien_foods}")



# foods with low protien
lowest_protien = min(float(food.get("protein")) for food in data)
low_protien_foods = [food.get("food_name") for food in data if float(food.get("protein")) == lowest_protien]
# print(f"low_protien_foods : {low_protien_foods}")



# which category food has high average protien content
category_wise_protien = {}
for food in data:
    category = food.get("category")
    protien = float(food.get("protein"))

    if category in category_wise_protien:
        category_wise_protien[category] += protien
    else:
        category_wise_protien[category] = protien

average_protien_in_categories = {c : round(p/all_category_list.count(c),2) for c,p in category_wise_protien.items()}
high_average_protien_category = [c for c, p in average_protien_in_categories.items() if p == max(average_protien_in_categories.values())]
# print("high_average_protien_category : ",high_average_protien_category)


# add a column
# Protein (g per 100g)	Protein Level 0–5 g,	 Low protein,  5–10 g	Moderate protein,  10–20 g	Good protein

#adding new key to data dictionary

for food in data:
    protein = float(food.get("protein"))
    if protein < 5:
        food["protien_level"] = "low"
    elif protein < 10:
        food["protien_level"] = "moderate"
    elif protein < 20:
        food["protien_level"] = "Good"

fieldnames = data[0].keys()
fw = open(file_path, "w", newline="")
writer = csv.DictWriter(fw, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(data)