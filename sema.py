import csv


with open("input.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["urls"])
