vehicles = [
    {"name": "Swift", "brand": "Maruti Suzuki", "price": 650000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Baleno", "brand": "Maruti Suzuki", "price": 820000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Creta", "brand": "Hyundai", "price": 1500000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "i20", "brand": "Hyundai", "price": 950000, "model": 2021, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Seltos", "brand": "Kia", "price": 1600000, "model": 2023, "color": "Silver", "fuel_type": "Diesel"},
    {"name": "Sonet", "brand": "Kia", "price": 1200000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Harrier", "brand": "Tata", "price": 1900000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "Nexon", "brand": "Tata", "price": 1200000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Punch", "brand": "Tata", "price": 800000, "model": 2023, "color": "Green", "fuel_type": "Petrol"},
    {"name": "XUV700", "brand": "Mahindra", "price": 2200000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Thar", "brand": "Mahindra", "price": 1700000, "model": 2022, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Scorpio N", "brand": "Mahindra", "price": 2000000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "City", "brand": "Honda", "price": 1500000, "model": 2021, "color": "Silver", "fuel_type": "Petrol"},
    {"name": "Amaze", "brand": "Honda", "price": 900000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Kiger", "brand": "Renault", "price": 800000, "model": 2021, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Duster", "brand": "Renault", "price": 1300000, "model": 2020, "color": "Brown", "fuel_type": "Diesel"},
    {"name": "EcoSport", "brand": "Ford", "price": 1100000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Endeavour", "brand": "Ford", "price": 3600000, "model": 2020, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Altroz", "brand": "Tata", "price": 950000, "model": 2022, "color": "Golden", "fuel_type": "Petrol"},
    {"name": "Venue", "brand": "Hyundai", "price": 1300000, "model": 2023, "color": "Red", "fuel_type": "Petrol"}
]

# display vehcle names whose color = red
print("red_color_vehicles : ",end="")
red_color_vehicles = [vehicle.get("name") for vehicle in vehicles if vehicle.get("color") == "Red"]
print(red_color_vehicles)

# display vehicles names  whose model 2022
print("model_2022_vehicles : ",end="")
model_2022_vehicles = [vehicle.get("name") for vehicle in vehicles if vehicle.get("model") == 2022]
print(model_2022_vehicles)

# display diesel vehile names
print("diesel_vehicles : ",end="")
diesel_vehicles = [vehicle.get("name") for vehicle in vehicles if vehicle.get("fuel_type") == "Diesel"]
print(diesel_vehicles)

# display all vehicle price
print("all vehicle price : ",end="")
all_vehicles_price = {vehicle.get("name") : vehicle.get("price") for vehicle in vehicles}
print(all_vehicles_price)

# display vehicle names whose price > 10lac
print("vehicles_price_gt_10lakh : ",end="")
vehicles_price_gt_10lakh = [vehicle.get("name") for vehicle in vehicles if vehicle.get("price") > 1000000]
print(vehicles_price_gt_10lakh)

# display tata vehicle names
print("tata_vehicles : ",end="")
tata_vehicles = [vehicle.get("name") for vehicle in vehicles if vehicle.get("brand") == "Tata"]
print(tata_vehicles)

# display tata vecle whose model 2022
print("tata_2022_model_vehicles : ",end="")
tata_2022_model_vehicles = [vehicle.get("name") for vehicle in vehicles if vehicle.get("brand") == "Tata" and vehicle.get("model") == 2022]
print(tata_2022_model_vehicles)

# display vehcle availabe at lowest price
lowest_price = min(vehicle.get("price") for vehicle in vehicles)
print("lowest_price_vehicle : ",end="")
lowest_price_vehicle = {vehicle.get("name") : lowest_price for vehicle in vehicles if vehicle.get("price") == lowest_price}
print(lowest_price_vehicle)

# dsipaly prices of maruthi suzuki vehicles
print("maruthi_suzuki_vehicles_price : ",end="")
maruthi_suzuki_vehicles_price = {vehicle.get("name") : vehicle.get("price") for vehicle in vehicles if vehicle.get("brand") == "Maruti Suzuki"}
print(maruthi_suzuki_vehicles_price)

# display hundayi vehicle names avaiale at > 5lac
print("hyundai_vehicle_gt_5_lakh : ",end="")
hyundai_vehicle_gt_5_lakh = {vehicle.get("name") : vehicle.get("price") for vehicle in vehicles if vehicle.get("brand") == "Hyundai" and vehicle.get("price") > 500000}
print(hyundai_vehicle_gt_5_lakh)

# display vehicle names whose model in range of 2022 - 2024
print("vehicles_model_in_range_2022_2024 : ",end="")
vehicles_model_in_range_2022_2024 = [vehicle.get("name") for vehicle in vehicles if vehicle.get("model") in range(2022, 2024)]
print(vehicles_model_in_range_2022_2024)

# which brand have most number of vehicle
brand_vehicle_count = {}
print("Brand with most vehicle : ",end="")
for vehicle in vehicles:
    brand = vehicle.get("brand")
    if brand not in brand_vehicle_count:
        brand_vehicle_count[brand] = 0
    brand_vehicle_count[brand] += 1

most_brand = max(brand_vehicle_count, key=brand_vehicle_count.get)

print(most_brand, ":" ,brand_vehicle_count[most_brand])


# costly vehicle availabe in mahindra and tata
print("costly_vehicle_in_mahindra_and_tata : ",end="")
mahindra_costly_vehicle_price = max(vehicle.get("price") for vehicle in vehicles if vehicle.get("brand") == "Mahindra")
tata_costly_vehicle_price = max(vehicle.get("price") for vehicle in vehicles if vehicle.get("brand") == "Tata")
costly_vehicle_in_mahindra_and_tata = {vehicle.get("name") : vehicle.get("price") for vehicle in vehicles
                                        if (vehicle.get("brand") == "Mahindra" and vehicle.get("price") == mahindra_costly_vehicle_price)
                                       or (vehicle.get("brand") == "Tata") and vehicle.get("price") == tata_costly_vehicle_price}

print(costly_vehicle_in_mahindra_and_tata)


# which model has most number of vehicles
model_vehicle_count = {}

for vehicle in vehicles:
    model = vehicle.get("model")

    if model in model_vehicle_count:
        model_vehicle_count[model] += 1
    else:
        model_vehicle_count[model] = 1

most_num_model = max(num for num in model_vehicle_count)
print("most_num_model = ",end="")
print(most_num_model, ":" ,model_vehicle_count[most_num_model])
