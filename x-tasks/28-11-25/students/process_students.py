students_report_path = "x-tasks/28-11-25/students/python_basics_report.csv"

fr_students_report = open(students_report_path, "r")

import csv

reader = csv.DictReader(fr_students_report)
data = [row for row in reader]
fr_students_report.close()
# print(data)

# for s in data :
#     print(s)


total_students = len(data)
# print(f"Total students : {total_students}")


names = [s.get("NAME") for s in data]
# print(names)

python_batch_students = [s for s in data if s.get("BATCH") == "Python"]
# print(python_batch_students)

present_percentage_100_students = [s.get("NAME") for s in data if s.get("PRESENT_%") == "100"]
# print(present_percentage_100_students)

name_mcq1_mark = {s.get("NAME") : s.get("MCQ1") for s in data}
# print(name_mcq1_mark)

overall_list = {s.get("NAME") : float(s["OVERALL"]) for s in data if s["OVERALL"].replace('.', '', 1).isdigit()}
highest_overall = max(overall_list.values())
top_performer = [s.get("NAME") for s in data if s.get("OVERALL") == str(highest_overall)]
# print(f"Top performer : {top_performer}")

less_than_30_perc = [n for n, v in overall_list.items() if v < 30]
# print(less_than_30_perc)

empty_column_students = [s.get("NAME") for s in data if "-" in s.values()]
# print(empty_column_students)


# new_student = { 'NAME': 'surya', 'MCQ_XOBIN': '63.53', 'PYTHON_BASICS_%': '50',
#                 'OVERALL': '76.77', 'MCQ1': '20', 'MCQ2': '20', 'TASK_COUNT': '10',
#                 'TASK_%': '45.5', 'HACKERRANK': '5', 'PRESENT_COUNT': '29', 'PRESENT_%': '90.6',
#                 'ABSENT_COUNT': '3', 'ABSENT_%': '9.4', 'BATCH': 'Python'}


all_batches_list = [s.get("BATCH") for s in data]
# print(f"Total python students = {all_batches_list.count("Python")}")
# print(f"Total Data Science students = {all_batches_list.count("Data Science")}")

absents_perc_names = {s.get("NAME") : float(s.get("ABSENT_%") ) for s in data if s["ABSENT_%"].replace('.', '', 1).isdigit()}
absents_perc_gt_20_names = [n for n, a in absents_perc_names.items() if a > 20]
gt_20_absent_full_data = [s for s in data if s.get("NAME") in absents_perc_gt_20_names]
# print(gt_20_absent_full_data)

sorted_overall_path = "x-tasks/28-11-25/students/sorted_overall.csv"
fw_sorted_overall = open(sorted_overall_path, "w")

def to_number(v):
    try:
        return float(v)
    except:
        return 0

sorted_data = sorted(data, key=lambda k: to_number(k.get("OVERALL")), reverse=True)

for row in sorted_data:
    fw_sorted_overall.write(str(row) + "\n")


#batch wise files
python_batch_path = "x-tasks/28-11-25/students/python_batch.csv"

with open(python_batch_path, "w", newline="") as fw:
    # Use the same field names as your original data
    fieldnames = data[0].keys()
    writer = csv.DictWriter(fw, fieldnames=fieldnames)

    writer.writeheader()  # write CSV headers

    for row in data:
        if row.get("BATCH") == "Python":
            writer.writerow(row)


data_science_batch_path = "x-tasks/28-11-25/students/data_science_batch.csv"
fw_data_science_batch = open(data_science_batch_path, "w")

with open(data_science_batch_path, "w", newline="") as fw:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(fw, fieldnames=fieldnames)

    writer.writeheader()

    for row in data:
        if row.get("BATCH") == "Data Science":
            writer.writerow(row)





rank_list_path = "x-tasks/28-11-25/students/rank_list.csv"
sorted_overall = sorted(overall_list, key=lambda k: overall_list.get(k), reverse=True)

with open(rank_list_path, "w", newline="") as fw:
    fieldnames = list(data[0].keys()) + ["RANK"]
    writer = csv.DictWriter(fw, fieldnames=fieldnames)

    writer.writeheader()

    for row in data:
        name = row["NAME"]
        if name in sorted_overall:
            rank = sorted_overall.index(name) + 1

            new_row = row.copy()
            new_row["RANK"] = rank

            writer.writerow(new_row)

def average(lst):
    sum = 0
    num_of_elements = len(lst)
    for n in lst:
        sum += n
    average = round(sum/num_of_elements,2)
    return average

# Average MCQ_XOBIN for Python batch
python_batch_mcq_xobin = [float(s.get("MCQ_XOBIN")) for s in data if s.get("BATCH") == "Python" and s.get("MCQ_XOBIN").replace(".","",1).isdigit()]
python_batch_mcq_xobin_average = average(python_batch_mcq_xobin)
print(f"python_batch_mcq_xobin_average : {python_batch_mcq_xobin_average}")

# Average MCQ_XOBIN for Data Science batch
data_science_batch_mcq_xobin = [float(s.get("MCQ_XOBIN")) for s in data if s.get("BATCH") == "Data Science" and s.get("MCQ_XOBIN").replace(".","",1).isdigit()]
data_science_batch_mcq_xobin_average = average(data_science_batch_mcq_xobin)
print(f"data_science_batch_mcq_xobin_average : {data_science_batch_mcq_xobin_average}")

# Average OVERALL for both batches
overall_both_batch = [float(s.get("OVERALL")) for s in data if s.get("OVERALL").replace(".", "", 1).isdigit()]
overall_both_batch_average = average(overall_both_batch)
print(f"overall_both_batch_average : {overall_both_batch_average}")

