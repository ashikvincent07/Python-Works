hacker_rak=[
    {"name":"abijith","count":4},
    {"name":"adith","count":2},
    {"name":"aadith","count":5},
    {"name":"adwaith","count":4},
    {"name":"amala","count":9},
    {"name":"arun","count":7},
    {"name":"ashiq","count":9},
    {"name":"fayaz","count":0},
    {"name":"felix","count":5},
    {"name":"harshit","count":4},
    {"name":"neenu","count":8},
    {"name":"saniya","count":7},
    {"name":"sarath","count":9},
    {"name":"SIVANANDANA","count":6},
    {"name":"sona","count":7},
    {"name":"vivek","count":2},
    {"name":"vrinda","count":7},
]

sort_student_count = sorted(hacker_rak, key = lambda s: s.get("count"))
print(sort_student_count)

most_count_students = [s.get("name") for s in hacker_rak if s.get("count") == max(s.get("count") for s in hacker_rak)]
print(most_count_students)

lowest_count_students = [s.get("name") for s in hacker_rak if s.get("count") == min(s.get("count") for s in hacker_rak)]
print(lowest_count_students)
