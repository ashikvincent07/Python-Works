import csv

class IndianFoodAnalysis:

    def __init__(self):
        file_path = "x-tasks/29-12-25/indian_food.csv"
        with open(file_path, "r", encoding="utf-8") as fr:
            reader = csv.DictReader(fr)
            self.data = list(reader)

    # 1. Which diet type has the highest number of dishes?
    def diet_distribution(self):
        diet_count = {}

        for food in self.data:
            diet = food.get("diet")
            diet_count[diet] = diet_count.get(diet, 0) + 1

        print("Diet distribution:", diet_count)

    # 2. Which region has the highest number of dishes?
    def region_wise_dishes(self):
        region_count = {}

        for food in self.data:
            region = food.get("region")
            region_count[region] = region_count.get(region, 0) + 1

        print("Region wise dishes:", region_count)

    # 3. Which state has the maximum number of dishes?
    def state_wise_dishes(self):
        state_count = {}

        for food in self.data:
            state = food.get("state")
            state_count[state] = state_count.get(state, 0) + 1

        max_state = max(state_count, key=state_count.get)
        print("State with maximum dishes:", max_state)

    # 4. Which course type is most common?
    def most_common_course(self):
        course_count = {}

        for food in self.data:
            course = food.get("course")
            course_count[course] = course_count.get(course, 0) + 1

        print("Course distribution:", course_count)

    # 5. Which flavor profile appears most frequently?
    def most_common_flavor(self):
        flavor_count = {}

        for food in self.data:
            flavor = food.get("flavor_profile")
            flavor_count[flavor] = flavor_count.get(flavor, 0) + 1

        print("Flavor profile distribution:", flavor_count)

    # 6. Which dishes require the longest average preparation time?
    def average_prep_time_by_course(self):
        course_time = {}
        course_count = {}

        for food in self.data:
            prep_time = food.get("prep_time")
            course = food.get("course")

            if prep_time.isdigit():
                course_time[course] = course_time.get(course, 0) + int(prep_time)
                course_count[course] = course_count.get(course, 0) + 1

        avg_prep = {c: course_time[c] / course_count[c] for c in course_time}
        print("Average preparation time by course:", avg_prep)

    # 7. Which region has the highest average cooking time?
    def average_cook_time_by_region(self):
        region_time = {}
        region_count = {}

        for food in self.data:
            cook_time = food.get("cook_time")
            region = food.get("region")

            if cook_time.isdigit():
                region_time[region] = region_time.get(region, 0) + int(cook_time)
                region_count[region] = region_count.get(region, 0) + 1

        avg_cook = {r: region_time[r] / region_count[r] for r in region_time}
        print("Average cooking time by region:", avg_cook)

    # 8. Do vegetarian dishes outnumber non-vegetarian dishes?
    def veg_vs_nonveg(self):
        diet_count = {}

        for food in self.data:
            diet = food.get("diet")
            diet_count[diet] = diet_count.get(diet, 0) + 1

        print("Veg vs Non-Veg count:", diet_count)

    # 9. Which state has the highest average preparation time?
    def highest_avg_prep_time_state(self):
        state_time = {}
        state_count = {}

        for food in self.data:
            prep_time = food.get("prep_time")
            state = food.get("state")

            if prep_time.isdigit():
                state_time[state] = state_time.get(state, 0) + int(prep_time)
                state_count[state] = state_count.get(state, 0) + 1

        avg_prep = {s: state_time[s] / state_count[s] for s in state_time}
        max_state = max(avg_prep, key=avg_prep.get)

        print("State with highest average prep time:", max_state)

    # 10. Which region has the most variety of courses?
    def course_variety_by_region(self):
        region_courses = {}

        for food in self.data:
            region = food.get("region")
            course = food.get("course")

            if region not in region_courses:
                region_courses[region] = set()

            region_courses[region].add(course)

        variety_count = {r: len(c) for r, c in region_courses.items()}
        print("Course variety by region:", variety_count)



indian_food = IndianFoodAnalysis()

# indian_food.diet_distribution()
# indian_food.region_wise_dishes()
# indian_food.state_wise_dishes()
# indian_food.most_common_course()
# indian_food.most_common_flavor()
# indian_food.average_prep_time_by_course()
# indian_food.average_cook_time_by_region()
# indian_food.veg_vs_nonveg()
# indian_food.highest_avg_prep_time_state()
indian_food.course_variety_by_region()