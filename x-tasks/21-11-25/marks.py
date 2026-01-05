marks = {
"Rahul": {"math": 85, "science": 90},
"Anita": {"math": 78, "science": 88}
}

#  science mark of "Anita".

for k, v in marks.items():

    if k == "Anita" :
        print(v.get("science"))