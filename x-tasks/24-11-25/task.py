taskreport=[
    {"name":"Abin","task_count":14,"mcq_score":19},
    {"name":"Adhil","task_count":13,"mcq_score":16},
    {"name":"Adhnan","task_count":13,"mcq_score":9},
    {"name":"Aryananda","task_count":16,"mcq_score":10},
    {"name":"Clairin","task_count":18,"mcq_score":12},
    {"name":"Joji","task_count":19,"mcq_score":23},
    {"name":"Libin","task_count":17,"mcq_score":20},
    {"name":"Lijo","task_count":15,"mcq_score":13},
    {"name":"shejeer","task_count":8,"mcq_score":11},
    {"name":"shafi","task_count":10,"mcq_score":18},
    {"name":"Resin","task_count":13,"mcq_score":20},
    {"name":"Sreelakshmi","task_count":14,"mcq_score":0},
    {"name":"Thamanna","task_count":1,"mcq_score":20},
    {"name":"Varshana","task_count":1,"mcq_score":11},
    {"name":"Abhijith ","task_count":10,"mcq_score":21},
    {"name":"Adith","task_count":1,"mcq_score":17},
    {"name":"Adithyan","task_count":3,"mcq_score":16},
    {"name":"Adwaid","task_count":3,"mcq_score":8},
    {"name":"Agnes","task_count":4,"mcq_score":19},
    {"name":"Amala","task_count":12,"mcq_score":18},
    {"name":"Arun","task_count":6,"mcq_score":20},
    {"name":"Ashik","task_count":20,"mcq_score":24},
    {"name":"Fayas","task_count":0,"mcq_score":0},
    {"name":"Felix","task_count":4,"mcq_score":15},
    {"name":"Harshithraj","task_count":7,"mcq_score":21},
    {"name":"Neenu","task_count":18,"mcq_score":21},
    {"name":"Saniya","task_count":20,"mcq_score":22},
    {"name":"Sharath","task_count":18,"mcq_score":22},
    {"name":"Sivanandhana","task_count":8,"mcq_score":15},
    {"name":"Sona","task_count":20,"mcq_score":19},
    {"name":"Vivek","task_count":7,"mcq_score":21},
    {"name":"Vrindha","task_count":8,"mcq_score":13}
]

# descending order sort based on task_count
# print("*************** sort_by_task_count *****************")
sort_by_task_count = sorted(taskreport, key = lambda s: s.get("task_count"), reverse = True)
name_task_count = [{s.get("name") : s.get("task_count")} for s in sort_by_task_count]
# print(name_task_count)
# print("*****************************************************")

# descending order sort based on mcq_score
# print("*************** sort_by_mcq_score *****************")
sort_by_mcq_score = sorted(taskreport, key = lambda s: s.get("mcq_score"), reverse = True)
name_mcq_score= [{s.get("name") : s.get("mcq_score")} for s in sort_by_task_count]
# print(name_mcq_score)
# print("*****************************************************")

# # mcq_topper
# print("*************** mcq_toppers *****************")
mcq_topper = [{s.get("name") : s.get("mcq_score")} for s in taskreport if s.get("mcq_score") == max(s.get("mcq_score") for s in sort_by_mcq_score)]
# print(mcq_topper)
# print("*****************************************************")

# most_task_completed_students
# print("*************** most_task_completed_students *****************")
most_task_completed_students = [{s.get("name") : s.get("task_count")} for s in taskreport if s.get("task_count") == max(s.get("task_count") for s in sort_by_task_count)]
# print(most_task_completed_students)
# print("*****************************************************")

# mcq passed students
print("*************** mcq_passed_students *****************")
mcq_passed_students = [s.get("name") for s in taskreport if s.get("mcq_score") >= 10]
print(mcq_passed_students)
print("*****************************************************")
