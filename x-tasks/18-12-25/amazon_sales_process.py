import csv

class AmazonSales2025INR:

    def __init__(self):
        file_path = "x-tasks/18-12-25/amazon_sales_2025_INR_cleaned.csv"

        with open(file_path, "r", encoding="utf-8") as fr:
            reader = csv.DictReader(fr)
            self.data = list(reader)

    # Which product category generates the highest total revenue, and how does it compare to the overall average category revenue?
    