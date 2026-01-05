import csv

class HeartDiseasePrediction:

    def __init__(self):
        file_path = "x-tasks/16-12-25/task-2/Heart_Disease_Prediction.csv"
        with open(file_path, "r") as fr:
            reader = csv.DictReader(fr)
            self.data = list(reader)

    
    # Which age group has the highest average risk of heart disease, and how does it compare to the overall average risk?
    def highest_average_heart_disease_risk(self):

        age_count = {}
        age_risk_count = {}

        for p in self.data:
            age = p.get("Age")
            heart_disease = p.get("Heart Disease")

            age_count[age] = age_count.get(age, 0) + 1
            if heart_disease == "Presence":
                age_risk_count[age] = age_risk_count.get(age, 0) + 1

        average_age_risk = {a : age_risk_count.get(a) / age_count.get(a) for a in age_risk_count}

        max_average_age_risk = max(average_age_risk.values())

        max_average_age = [a for a, r in average_age_risk.items() if r == max_average_age_risk]

        # print(f"Age with highest heart disease risk : {max_average_age[0]} Risk average : {max_average_age_risk}")

        heart_disease_all_list = [p for p in self.data if p.get("Heart Disease") == "Presence"]

        overall_risk_average = len(heart_disease_all_list) / len(self.data)

        # print(f"Overall risk average : {overall_risk_average}")

        # Do male or female patients show a higher prevalence of heart disease, and by what margin?

    def male_female_heart_disease(self):
        male_female_count = {}
        male_female_disease_count = {}

        for p in self.data:
            heart_disease = p.get("Heart Disease")
            gender = p.get("Sex")

            if gender == "1":
                male_female_count["male"] = male_female_count.get("male", 0) + 1
            else :
                male_female_count["female"] = male_female_count.get("female", 0) + 1

            if gender == "1" and heart_disease == "Presence":
                male_female_disease_count["male"] = male_female_disease_count.get("male", 0) + 1
            
            elif heart_disease == "Presence":
                male_female_disease_count["female"] = male_female_disease_count.get("female", 0) + 1
            
        male_female_average_risk = {g : male_female_disease_count.get(g) / male_female_count.get(g) for g in male_female_disease_count}

        print(f"male_female_average_risk : {male_female_average_risk}")
 

    
heart_disease_prediction_instance = HeartDiseasePrediction()

# heart_disease_prediction_instance.highest_average_heart_disease_risk()
heart_disease_prediction_instance.male_female_heart_disease()





