school = {
"class10": {
"teacher": "Mr. Kumar",
"students": {"S1": "Ravi", "S2": "Meena"}
},
"class9": {
"teacher": "Mrs. Sharma",
"students": {"S1": "Amit", "S2": "Priya"}
}
}


# class 9 teacher

for k, v in school.items():
    if k == "class9":
        print(v.get("teacher"))