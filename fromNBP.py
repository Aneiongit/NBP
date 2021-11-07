import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()


with open("currency.csv", "w", encoding="UTF8", newline="") as csvfile:
    header = ["currency", "code", "bid", "ask"]
    writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=header)
    writer.writeheader()
    for i in data[0]["rates"]:
        writer.writerow(i)
