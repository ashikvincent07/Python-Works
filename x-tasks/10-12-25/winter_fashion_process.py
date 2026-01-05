"""
Docstring for x-tasks.10-12-25.winter_fashion_process

1. Which fashion category has the highest average **customer rating** across all winter seasons?
2. Which **brand** offers the most expensive products on average in the dataset?
3. Which **material** is associated with the highest **popularity score** overall?
4. Which **gender segment** shows the lowest average **popularity score** for winter products?
5. Which **style** category has the highest proportion of items marked as **“Trending”**?
6. Which **season year** has the highest average **product price**?
7. Which **color** appears most frequently among products labeled as **Outdated**?
8. Which **category** records the widest range of **customer ratings**?
9. Which **brand** has the highest average **popularity score** within the **Unisex** segment?
10. Which **material** has the lowest average **customer rating** across the dataset?

"""



import csv

file_path = "x-tasks/10-12-25/Winter_Fashion_Trends_Dataset.csv"

with open(file_path, "r", encoding="utf-8") as fr:
    reader = csv.DictReader(fr)
    data = list(reader)

#  Which fashion category has the highest average **customer rating** across all winter seasons
category_count = {}
for cloth in data:
    category = cloth.get("Category")

    if category in category_count:
        category_count[category] += 1

    else:
        category_count[category] = 1

category_cust_rating = {}
for cloth in data:
    customer_rating = float(cloth.get("Customer_Rating"))
    category = cloth.get("Category")

    if category in category_cust_rating:
        category_cust_rating[category] += customer_rating

    else:
        category_cust_rating[category] = customer_rating

category_cust_rating_average = {}
for c, r in category_cust_rating.items():
    category_cust_rating_average[c] = r/category_count.get(c)

max_category_cust_rating_average = [c for c, r in category_cust_rating_average.items() if r == max(category_cust_rating_average.values())]

# print(f"fashion category has the highest average **customer rating** across all winter seasons : {max_category_cust_rating_average[0]}")





# add column Budget: below $293, Mid-range: $293 – $446, Premium: $446 – $632,  Expensive: above $632 based on price
for cloth in data:
    price_usd = float(cloth.get("Price(USD)"))

    if price_usd < 293:
        cloth["price_category"] = "Budget"
    elif price_usd < 446:
        cloth["price_category"] = "Mid-range"
    elif price_usd < 632:
        cloth["price_category"] = "Premium"
    else:
        cloth["price_category"] = "Expensive"

fieldnames = list(data[0].keys())

# with open(file_path, "w", newline= "", encoding="utf-8") as fw:
#     writer = csv.DictWriter(fw, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)



# Which **brand** offers the most expensive products on average in the dataset?
brand_count = {}
for cloth in data:
    brand = cloth.get("Brand")

    if brand in brand_count:
        brand_count[brand] += 1
    else:
        brand_count[brand] = 1

expensive_cloth_brand = {}
for cloth in data:
    price_category = cloth.get("price_category")
    brand = cloth.get("Brand")

    if price_category == "Expensive":
        if brand in expensive_cloth_brand:
            expensive_cloth_brand[brand] += 1
        else:
            expensive_cloth_brand[brand] = 1

average_expensive_cloth_brand = {}
for b, c in expensive_cloth_brand.items():
    average_expensive_cloth_brand[b] = round((c/brand_count.get(b)) * 100, 2)

max_expensive_cloth_brand = [b for b, c in average_expensive_cloth_brand.items() if c == max(average_expensive_cloth_brand.values())]
# print(f"**brand** offers the most expensive products on average : {max_expensive_cloth_brand[0]}")




# Which **material** is associated with the highest **popularity score** overall?
max_popularity_score = max(float(cloth.get("Popularity_Score")) for cloth in data)
material_with_high_popularity_score = [cloth.get("Material") for cloth in data if float(cloth.get("Popularity_Score")) == max_popularity_score]
# print(f"material_with_high_popularity_score : {material_with_high_popularity_score}")




# Which **gender segment** shows the lowest average **popularity score** for winter products?
gender_count = {}
for cloth in data:
    gender = cloth.get("Gender")
    if gender in gender_count:
        gender_count[gender] += 1
        
    else :
        gender_count[gender] = 1

gender_popularity_score = {}
for cloth in data:
    gender = cloth.get("Gender")
    popularity_score = float(cloth.get("Popularity_Score"))
    if gender in gender_popularity_score:
        gender_popularity_score[gender] += popularity_score

    else:
        gender_popularity_score[gender] = popularity_score

average_gender_popularity_score = {}
for g, p in gender_popularity_score.items():
    average_gender_popularity_score[g] = p/gender_count.get(g)

lowest_average_gender_popularity_score = [g for g, p in average_gender_popularity_score.items() if p == min(average_gender_popularity_score.values())]
# print(f"lowest_average_gender_popularity_score : {lowest_average_gender_popularity_score}")


# Which **style** category has the highest proportion of items marked as **“Trending”**?
style_trending_count = {}
for cloth in data:
    style = cloth.get("Style")
    trend_status = cloth.get("Trend_Status")

    if trend_status == "Trending":
        if style in style_trending_count:
            style_trending_count[style] += 1
        else:
            style_trending_count[style] = 1

style_with_highest_trending = [s for s, t in style_trending_count.items() if t == max(style_trending_count.values())]
# print(f"Styel category wwith highest item marked as trend:  {style_with_highest_trending[0]}")



# Which **season year** has the highest average **product price**?
season_year_count = {}
for cloth in data:
    season_year = cloth.get("Season")

    if season_year in season_year_count:
        season_year_count[season_year] += 1

    else:
        season_year_count[season_year] = 1

season_year_price = {}
for cloth in data:
    season_year = cloth.get("Season")
    price = float(cloth.get("Price(USD)"))

    if season_year in season_year_price:
        season_year_price[season_year] += price
    
    else:
        season_year_price[season_year] = price

average_season_year_price = {}
for y, p in season_year_price.items():
    average_season_year_price[y] = p/season_year_count.get(y)

max_average_season_year_price = [s for s, p in average_season_year_price.items() if p == max(average_season_year_price.values())]
print(f"**season year** has the highest average **product price** : {max_average_season_year_price[0]}")





    

















