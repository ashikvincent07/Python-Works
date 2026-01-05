import csv
class AiImpact:
    data : list

    def __init__(self):
        file_path = "object-oriented-programming/ai-impact-on-jobs-2030/AI_Impact_on_Jobs_2030.csv"
        fr = open(file_path, "r", encoding="utf-8")
        reader = csv.DictReader(fr)
        self.data = list(reader)

    def total_records(self):
        print(f"Total records = {len(self.data)}")

    def all_jobs(self):
        all_jobs = [j.get("Job_Title") for j in self.data]
        print(set(all_jobs))

    def first_record(self):
        print(f"First record : {self.data[0]}")
        


ai_impact_instance1 = AiImpact()
ai_impact_instance1.total_records()
ai_impact_instance1.all_jobs()
ai_impact_instance1.first_record()