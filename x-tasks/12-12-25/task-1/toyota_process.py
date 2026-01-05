"""
1. Which Toyota fuelType has the highest average selling price across all years?
2. Which transmission type (Manual or Automatic) is associated with the lowest average mileage?
3. Which fuelType-year combination offers the best fuel efficiency (highest mpg)?
4. Which fuel type shows the widest price variation within the dataset?
5. Which engine size category is priced the highest on average?
6. Which fuelType has the highest tax cost relative to its average price?
7. Which manufacturing year provides the best price-to-mileage ratio (lowest cost per mile)?
8. Which transmission type leads to the highest resale value for newer fuelTypes (year >= 2017)?
9. Which fuelType has the most consistent pricing trend across different years?
10. Which fuel type delivers the highest mpg while maintaining a competitive price?
"""
import csv

file_path = "x-tasks/12-12-25/task-1/toyota.csv"

with open(file_path, "r") as fr:
    reader = csv.DictReader(fr)
    data = list(reader)


# 1. Which Toyota fuelType has the highest average selling price across all years?

fuelType_count = {}
for car in data:
    fuelType = car.get("fuelType")

    if fuelType in fuelType_count:
        fuelType_count[fuelType] += 1
    else:
        fuelType_count[fuelType] = 1

fuelType_price = {}
for car in data:
    fuelType = car.get("fuelType")
    price = int(car.get("price"))

    if fuelType in fuelType_price:
        fuelType_price[fuelType] += price
    else:
        fuelType_price[fuelType] = price

average_fuelType_price = {}
for m, p in fuelType_price.items():
    average_fuelType_price[m] = p/fuelType_count[m]

max_average_fuelType_price = [m for m, p in average_fuelType_price.items() if p == max(average_fuelType_price.values())] 

# print(f"max_average_fuelType_price : {max_average_fuelType_price[0]}")




# 2. Which transmission type (Manual or Automatic) is associated with the lowest average mileage?
transmission_count = {}
transmission_mileage = {}

for car in data:
    transmission = car.get("transmission")
    mileage = int(car.get("mileage"))

    if transmission != "Manual" and transmission != "Automatic":
        continue

    transmission_count[transmission] = transmission_count.get(transmission, 0) + 1

    transmission_mileage[transmission] = transmission_mileage.get(transmission, 0) + mileage

average_transmission_mileage = {t: transmission_mileage[t] / transmission_count[t]for t in transmission_mileage}

lowest = [t for t, m in average_transmission_mileage.items() if m == min(average_transmission_mileage.values())]

# print("lowest_average_transmission_mileage :", lowest[0])




# 3. Which fuelType-year combination offers the best fuel efficiency (highest mpg)?
highest_mpg = max(float(car.get("mpg")) for car in data)
fuelType_year_with_highest_mpg = {car.get("fuelType") : car.get("year") for car in data if float(car.get("mpg")) == highest_mpg}
# print(f"fuelType_year_with_highest_mpg : {fuelType_year_with_highest_mpg}")





# 4. Which fuel type shows the widest price variation within the dataset?
fuel_types = {car.get("fuelType") for car in data}

max_price_all_fuel_types = {}
min_price_all_fuel_types = {}
difference_price_all_fuel_types = {}

for fuel_type in fuel_types:
        max_price_all_fuel_types[fuel_type] = max(int(car.get("price")) for car in data if car.get("fuelType") == fuel_type)
        min_price_all_fuel_types[fuel_type] = min(int(car.get("price")) for car in data if car.get("fuelType") == fuel_type)
        difference_price_all_fuel_types[fuel_type] = max_price_all_fuel_types.get(fuel_type) - min_price_all_fuel_types.get(fuel_type)

widest_price_variation_fuel_type_wise = [f for f, d in difference_price_all_fuel_types.items() if d == max(difference_price_all_fuel_types.values())]
# print(f"widest_price_variation_fuel_type_wise : {widest_price_variation_fuel_type_wise[0]}")



# 5. Which engine size category is priced the highest on average?
engine_size_count = {}
engine_size_price = {}
for car in data:
    engine_size = car.get("engineSize")
    price = int(car.get("price"))

    engine_size_count[engine_size] = engine_size_count.get(engine_size, 0) + 1
    engine_size_price[engine_size] = engine_size_price.get(engine_size, 0) + price

average_engine_size_price = {e : p / engine_size_count.get(e) for e, p in engine_size_price.items()}

highest_average_engine_size_price = [e for e, p in average_engine_size_price.items() if p == max(average_engine_size_price.values())]

# print(f"highest_average_engine_size_price : {highest_average_engine_size_price[0]}")