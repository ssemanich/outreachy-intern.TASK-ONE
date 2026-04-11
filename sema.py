import csv
import requests

with open("input.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        url = row["urls"]
        try:
            response = requests.get(url)
            print(f"{url}: {response.status_code}")
        except requests.RequestException as e:
            print(f"{url}: Error - {e}")
