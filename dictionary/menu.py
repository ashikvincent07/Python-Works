menu_items = {
    "chappati" : 12, 
    "tea" : 15, 
    "biriyani" : 180, 
    "fresh lime" : 30, 
    "fried rice" : 160, 
    "chocolate shake" : 80
    }

for k in menu_items.keys():
    pass

# for k,v in menu_items.items():
#     print(f"{k} : {v}")

# for k,v in menu_items.items():

#     if v < 50:
#         print(k)

# price = 0
# costly_item = ""

# for k, v in menu_items.items():

#     if v >  price:
#         costly_item = k
#         price = v

# print(f"Costly item = {costly_item}")

# item_price = menu_items.get("tea", 0)

# print(item_price)

if "tea" in menu_items:
    menu_items["tea"] += 15

print(menu_items)