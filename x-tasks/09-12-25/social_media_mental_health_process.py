"""
Docstring for x-tasks.09-12-25.social_media_mental_health_process
1. Which social media platform shows the highest average anxiety and stress levels among users?
2. Which age group spends the most time on social media relative to their total daily screen time?
3. Which gender reports the lowest sleep hours on average across the dataset?
4. Which platform has users with the highest number of negative interactions?
5. Does increased daily screen time correlate more strongly with anxiety_level or stress_level?
6. Which group (by mental_state) has the highest average physical activity per day?
7. Which platform’s users show the largest gap between positive and negative interactions?
8. Are users with high mood_level concentrated on any specific platform or age group?
9. Which day or date range shows the highest average screen time across all users?
10. Which factor (sleep_hours, physical_activity_min, positive_interactions_count) appears most associated with a “Stressed” mental_state?
"""


import csv

file_path = "x-tasks/09-12-25/mental_health_social_media_dataset.csv"

with open(file_path, "r") as fr:
    reader = csv.DictReader(fr)
    data = list(reader)

platform_user_count = {}

for user in data:
    platform = user.get("platform")
    if platform in platform_user_count:
        platform_user_count[platform] += 1
    else:
        platform_user_count[platform] = 1

# 1. Which social media platform shows the highest average anxiety and stress levels among users?
platform_anxiety_level = {}

for user in data:
    platform = user.get("platform")
    anxiety_level = int(user.get("anxiety_level"))
    if platform in platform_anxiety_level:
        platform_anxiety_level[platform] += anxiety_level
    else:
        platform_anxiety_level[platform] = anxiety_level

platform_anxiety_level_average = {}

for p, a in platform_anxiety_level.items():
    platform_anxiety_level_average[p] = round(a/platform_user_count.get(p), 2)

platform_stress_level = {}

for user in data:
    platform = user.get("platform")
    stress_level = int(user.get("stress_level"))
    if platform in platform_stress_level:
        platform_stress_level[platform] += stress_level
    else:
        platform_stress_level[platform] = stress_level

platform_stress_level_average = {}

for p, a in platform_stress_level.items():
    platform_stress_level_average[p] = round(a/platform_user_count.get(p), 2)

max_average_anxiety = [p for p, a in platform_anxiety_level_average.items() if a == max(platform_anxiety_level_average.values())]
max_average_stress = [p for p, a in platform_stress_level_average.items() if a == max(platform_stress_level_average.values())]

# print(f"Social media platform which has highest average anxiety : {max_average_anxiety[0]}")
# print(f"Social media platform which has highest average stress : {max_average_stress[0]}")



# 2. Which age group spends the most time on social media relative to their total daily screen time?
age_user_count = {}
for user in data:
    age = user.get("age")
    if age in age_user_count:
        age_user_count[age] += 1
    else:
        age_user_count[age] = 1

age_screen_time = {}
for user in data:
    age = user.get("age")
    daily_screen_time_min = int(user.get("daily_screen_time_min"))
    if age in age_screen_time:
        age_screen_time[age] += daily_screen_time_min
    else:
        age_screen_time[age] = daily_screen_time_min

age_screen_time_average = {}
for a, s in age_screen_time.items():
    age_screen_time_average[a] = s/age_user_count.get(a)

max_age_screen_time_average = [a for a, s in age_screen_time_average.items() if s == max(age_screen_time_average.values())]
# print(f"age group spends the most time on social media relative to their total daily screen time : {max_age_screen_time_average[0]}")


#3. Which gender reports the lowest sleep hours on average across the dataset?
gender_count = {}
for user in data:
    gender = user.get("gender")
    if gender in gender_count:
        gender_count[gender] += 1
    else:
        gender_count[gender] = 1

gender_sleep_hours = {}
for user in data:
    gender = user.get("gender")
    sleep_hours = float(user.get("sleep_hours"))

    if gender in gender_sleep_hours:
        gender_sleep_hours[gender] += sleep_hours
    else:
        gender_sleep_hours[gender] = sleep_hours

gender_sleep_hours_average = {}
for g, s in gender_sleep_hours.items():
    gender_sleep_hours_average[g] = s/gender_count.get(g)

max_gender_sleep_hours_average = [g for g, s in gender_sleep_hours_average.items() if s == min(gender_sleep_hours_average.values())]
# print(f"gender reports the lowest sleep hours on average : {max_gender_sleep_hours_average[0]}")

# 4. Which platform has users with the highest number of negative interactions?
platform_negative_interaction = {}
for user in data:
    platform = user.get("platform")
    negative_interactions_count = int(user.get("negative_interactions_count"))

    if platform in platform_negative_interaction:
        platform_negative_interaction[platform] += negative_interactions_count
    else:
        platform_negative_interaction[platform] = negative_interactions_count

highest_platform_negative_interaction = [p for p, n in platform_negative_interaction.items() if n == max(platform_negative_interaction.values())]
# print(f"platform has users with the highest number of negative interactions : {highest_platform_negative_interaction[0]}")     




# 5. Which group (by mental_state) has the highest average physical activity per day?
mental_state_count = {}
for user in data:
    mental_state = user.get("mental_state")
    if mental_state in mental_state_count:
        mental_state_count[mental_state] += 1
    else:
        mental_state_count[mental_state] = 1

mental_state_physical_activity = {}
for user in data:
    physical_activity_min = int(user.get("physical_activity_min"))
    mental_state = user.get("mental_state")

    if mental_state in mental_state_physical_activity:
        mental_state_physical_activity[mental_state] += physical_activity_min
    else:
        mental_state_physical_activity[mental_state] = physical_activity_min

average_mental_state_physical_activity = {}
for m, p in mental_state_physical_activity.items():
    average_mental_state_physical_activity[m] = p/mental_state_count.get(m)

max_average_mental_state_physical_activity = [m for m, p in average_mental_state_physical_activity.items() if p == max(average_mental_state_physical_activity.values())]
print(f"mental state with highest average physical activity per day : {max_average_mental_state_physical_activity[0]}")







