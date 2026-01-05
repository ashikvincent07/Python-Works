import csv

class CovidAnalysis:

    def __init__(self):
        file_path = "x-tasks/05-01-26/country_wise_latest_covid.csv"
        with open(file_path, "r", encoding="utf-8") as fr:
            reader = csv.DictReader(fr)
            self.data = list(reader)

    # 1. Which country has the highest number of confirmed cases?
    def highest_confirmed_cases(self):
        country_cases = {}

        for row in self.data:
            country = row.get("Country/Region")
            cases = row.get("Confirmed")

            if cases.isdigit():
                country_cases[country] = int(cases)

        max_country = max(country_cases, key=country_cases.get)
        print("Country with highest confirmed cases:", max_country)

    # 2. Which country has the highest number of deaths?
    def highest_deaths(self):
        country_deaths = {}

        for row in self.data:
            country = row.get("Country/Region")
            deaths = row.get("Deaths")

            if deaths.isdigit():
                country_deaths[country] = int(deaths)

        max_country = max(country_deaths, key=country_deaths.get)
        print("Country with highest deaths:", max_country)

    # 3. Which country has the highest number of recovered cases?
    def highest_recoveries(self):
        country_recovered = {}

        for row in self.data:
            country = row.get("Country/Region")
            recovered = row.get("Recovered")

            if recovered.isdigit():
                country_recovered[country] = int(recovered)

        max_country = max(country_recovered, key=country_recovered.get)
        print("Country with highest recoveries:", max_country)

    # 4. Which WHO region has the highest total confirmed cases?
    def confirmed_cases_by_region(self):
        region_cases = {}

        for row in self.data:
            region = row.get("WHO Region")
            cases = row.get("Confirmed")

            if cases.isdigit():
                region_cases[region] = region_cases.get(region, 0) + int(cases)

        print("Confirmed cases by WHO region:", region_cases)

    # 5. Which WHO region has the highest total deaths?
    def deaths_by_region(self):
        region_deaths = {}

        for row in self.data:
            region = row.get("WHO Region")
            deaths = row.get("Deaths")

            if deaths.isdigit():
                region_deaths[region] = region_deaths.get(region, 0) + int(deaths)

        print("Deaths by WHO region:", region_deaths)

    # 6. Which WHO region has the highest average confirmed cases?
    def average_confirmed_by_region(self):
        region_total = {}
        region_count = {}

        for row in self.data:
            region = row.get("WHO Region")
            cases = row.get("Confirmed")

            if cases.isdigit():
                region_total[region] = region_total.get(region, 0) + int(cases)
                region_count[region] = region_count.get(region, 0) + 1

        avg_cases = {r: region_total[r] / region_count[r] for r in region_total}
        print("Average confirmed cases by region:", avg_cases)

    # 7. Which country has the highest active cases?
    def highest_active_cases(self):
        active_cases = {}

        for row in self.data:
            country = row.get("Country/Region")
            active = row.get("Active")

            if active.isdigit():
                active_cases[country] = int(active)

        max_country = max(active_cases, key=active_cases.get)
        print("Country with highest active cases:", max_country)

    # 8. Which WHO region has the highest total active cases?
    def active_cases_by_region(self):
        region_active = {}

        for row in self.data:
            region = row.get("WHO Region")
            active = row.get("Active")

            if active.isdigit():
                region_active[region] = region_active.get(region, 0) + int(active)

        print("Active cases by WHO region:", region_active)

    # 9. Which country has the highest death-to-confirmed ratio?
    def highest_death_ratio(self):
        death_ratio = {}

        for row in self.data:
            country = row.get("Country/Region")
            deaths = row.get("Deaths")
            confirmed = row.get("Confirmed")

            if deaths.isdigit() and confirmed.isdigit() and int(confirmed) > 0:
                death_ratio[country] = int(deaths) / int(confirmed)

        max_country = max(death_ratio, key=death_ratio.get)
        print("Country with highest death ratio:", max_country)

    # 10. How many countries belong to each WHO region?
    def country_count_by_region(self):
        region_count = {}

        for row in self.data:
            region = row.get("WHO Region")
            region_count[region] = region_count.get(region, 0) + 1

        print("Country count by WHO region:", region_count)


covid = CovidAnalysis()

# covid.highest_confirmed_cases()
# covid.highest_deaths()
# covid.highest_recoveries()
# covid.confirmed_cases_by_region()
# covid.deaths_by_region()
# covid.average_confirmed_by_region()
# covid.highest_active_cases()
# covid.active_cases_by_region()
# covid.highest_death_ratio()
covid.country_count_by_region()
