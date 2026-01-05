import csv

class DogBreeds:

    def __init__(self):
        file_path = "x-tasks/15-12-25/dog_breeds/dog_breeds.csv"
        with open(file_path, "r") as fr:
            reader = csv.DictReader(fr)
            data = list(data)


