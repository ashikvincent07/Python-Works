treasures = {"box1" : "gold", "box2" : "silver", "box3" : "diamond", "box4" : "platinum"}

treasures["box5"] = "irom"

if "box6" not in treasures:
    treasures["box6"] = "copper"

for k in treasures.keys(): # return keys
    print(f"{k}",end=", ")

print()

for v in treasures.values(): # return values
    print(f"{v}",end=", ")

print()

for k, v in treasures.items(): # return both keys and values
    print(f"{k} : {v}",end=", ")

print()

box_2_value = treasures.get("box9","Empty box") # return value if key exist else return None

print(box_2_value)

treasures.pop("box2")

print(treasures)
    
