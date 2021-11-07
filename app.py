from flask import Flask, render_template, request
import csv

currency = []
bid = []

with open("currency.csv", "r", encoding="UTF8", newline="") as csvfile:
    header = ["currency", "code", "bid", "ask"]
    reader = csv.DictReader(csvfile, delimiter=";", fieldnames=header)
    x = 0
    for i in reader:
        currency.append([x, i["currency"].title()])
        bid.append(i["bid"])
        x += 1

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def action():
    if request.method == "POST":
        option = int(request.form["option"][1:2])
        quantity = int(request.form.get("quantity"))
        bidd = float(bid[option])
        result = bidd * quantity
        return render_template("index.html", items=currency, p=result)

    return render_template("index.html", x=x,  items=currency)


if __name__ == "__main__":
    app.run(debug=True)
