file_path = "file-operations/carts/cart_items_100.csv"

fr = open(file_path, "r", encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = list(reader)

order_summary = {}

for o in data:
    title = o.get("title")
    qty = int(o.get("quantity", 0))

    if title in order_summary:
        order_summary[title] += qty

    else:
        order_summary[title] = qty

most_quantity_item = [{t:q} for t,q in order_summary.items() if q == max(order_summary.values())]
print(f"most_quantity_item : {most_quantity_item}")

least_quantity_item = [{t:q} for t,q in order_summary.items() if q == min(order_summary.values())]
print(f"least_quantity_item : {least_quantity_item}")

all_users_list = [o.get("user") for o in data]
user_order_count = {u : all_users_list.count(u) for u in set(all_users_list)}

most_ordered_user = [{u:c} for u,c in user_order_count.items() if c == max(user_order_count.values())]
print(f"most_ordered_user : {most_ordered_user}")

least_ordered_user = [{u:c} for u,c in user_order_count.items() if c == min(user_order_count.values())]
print(f"least_ordered_user : {least_ordered_user}")

