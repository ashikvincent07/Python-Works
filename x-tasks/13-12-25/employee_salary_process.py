import csv

class EmployeeSalary:
    def __init__(self):
        file_path = "x-tasks/13-12-25/employee_salary_dataset.csv"
        with open(file_path, "r") as fr:
            reader = csv.DictReader(fr)
            self.data = list(reader)

    # Which department has the highest average salary?
    def department_with_highest_average_salary(self):
        department_count = {}
        department_salary = {}

        for emp in self.data:
            department = emp.get("Department")
            salary = int(emp.get("Monthly_Salary"))

            department_count[department] = department_count.get(department, 0) + 1
            department_salary[department] = department_salary.get(department, 0) + salary

        average_department_salary = {d: department_salary.get(d) / department_count.get(d) for d in department_salary}

        max_avg_salary = max(average_department_salary.values())

        highest_departments = [d for d, s in average_department_salary.items() if s == max_avg_salary]

        print("Department(s) with highest average salary:", highest_departments[0])
        print("Average Salary:", max_avg_salary)

    
    # Which department shows the maximum salary variation?
    def department_with_high_salary_variation(self):
        all_departments = {emp.get("Department") for emp in self.data}

        departments_salary_diff = {}

        for dept in all_departments:
            max_salary = max(int(emp.get("Monthly_Salary")) for emp in self.data if emp.get("Department") == dept)
            min_salary = min(int(emp.get("Monthly_Salary")) for emp in self.data if emp.get("Department") == dept)

            departments_salary_diff[dept] = max_salary - min_salary

        max_salary_variation_dept = [d for d, s in departments_salary_diff.items() if s == max(departments_salary_diff.values())]

        print(f"max_salary_variation_dept : {max_salary_variation_dept[0]}")


    # What is the average salary by experience level?
    def average_salary_by_experience_level(self):
        experience_count = {}
        experience_salary = {}

        for emp in self.data:
            experience = emp.get("Experience_Years")
            salary = int(emp.get("Monthly_Salary"))

            experience_count[experience] = experience_count.get(experience, 0) + 1
            experience_salary[experience] = experience_salary.get(experience, 0) + salary
        
        average_experience_salary = {d : round(experience_salary.get(d) / experience_count.get(d), 2) for d in experience_salary}
        print(f"Average salary by experience level : {average_experience_salary}")


    # Which department contributes the most to total salary cost?

    def dept_most_total_salary(self):

        dept_salary = {}

        for emp in self.data:
            department = emp.get("Department")
            salary = int(emp.get("Monthly_Salary"))

            dept_salary[department] = dept_salary.get(department, 0) + salary

        dept_with_most_total_salary = [d for d, s in dept_salary.items() if s == max(dept_salary.values())]
        print(f"dept_with_most_total_salary : {dept_with_most_total_salary[0]}")

    
    # Identify the top 5 highest-paid employees and their departments.
    def top_5_salary_emp(self):

        emp_salary = {emp.get("EmployeeID") : int(emp.get("Monthly_Salary")) for emp in self.data}
        sorted_emp_salary = sorted(emp_salary, key=emp_salary.get, reverse=True)
        top_5_salary = sorted_emp_salary[:5]

        for id in top_5_salary:
            for emp in self.data:
                if id == emp.get("EmployeeID"):
                    print(f"Name : {emp.get("Name")}, Department : {emp.get("Department")}")

        






employee_salary_instance = EmployeeSalary()
# employee_salary_instance.department_with_highest_average_salary()
# employee_salary_instance.department_with_high_salary_variation()
# employee_salary_instance.average_salary_by_experience_level()
# employee_salary_instance.dept_most_total_salary()
# employee_salary_instance.top_5_salary_emp()




