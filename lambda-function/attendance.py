attendance=[

    {"name":"abin","attendance_count":28,"count":1},
    {"name":"aadhil","attendance_count":20,"count":2},
    {"name":"adhnan","attendance_count":20,"count":2},
    {"name":"arya","attendance_count":25,"count":5},
    {"name":"clairin","attendance_count":25,"count":4},
    {"name":"joji","attendance_count":26,"count":7},
    {"name":"libin","attendance_count":28,"count":7},
    {"name":"lijo","attendance_count":21,"count":2},
    {"name":"shajeer","attendance_count":27,"count":2},
    {"name":"shafi","attendance_count":28,"count":7},
    {"name":"resin","attendance_count":24,"count":3},
    {"name":"lakshmi","attendance_count":16,"count":6},
    {"name":"thammana","attendance_count":25,"count":1},
    {"name":"VARSHANA","attendance_count":8,"count":0},

]

attendance_count = lambda s: s.get("count")

print("sort_attendance : ",end="")
sort_attendance = sorted(attendance, key = lambda s: s.get("attendance_count"))
name_attendance = [{s.get("name") : s.get("attendance_count")} for s in sort_attendance]
print(name_attendance) 
print()

print("hacker_count_sort : ",end="")
hack_ranke_sort = sorted(attendance ,key= lambda s: s.get("count"))
name_hacker_count = [{s.get("name") : s.get("count")} for s in hack_ranke_sort]
print(name_hacker_count)
print()

print("most_attendance : ",end="")
most_attendance = [{s.get("name") : s.get("attendance_count")} for s in attendance if s.get("attendance_count") == max(s.get("attendance_count") for s in attendance)]
print(most_attendance)
print()

print("low_attendance : ",end="")
low_attendance = [{s.get("name") : s.get("attendance_count")} for s in attendance if s.get("count") == min(s.get("count") for s in attendance)]
print(low_attendance)
print()

print("most_hack_rank : ",end="")
most_hack_rank = [{s.get("name") : s.get("count")} for s in attendance if s.get("count") == max(s.get("count") for s in attendance)]
print(most_hack_rank)
print()

print("low_hack_rank : ",end="")
low_hack_rank = [{s.get("name") : s.get("count")} for s in attendance if s.get("count") == min(s.get("count") for s in attendance)]
print(low_hack_rank)
