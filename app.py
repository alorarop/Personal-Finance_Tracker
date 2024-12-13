from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store financial data
data = {
    "income": [],
    "expenses": [],
    "balance": 0,
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        transaction_type = request.form.get("type")
        amount = float(request.form.get("amount"))
        description = request.form.get("description")

        if transaction_type == "income":
            data["income"].append({"amount": amount, "description": description})
            data["balance"] += amount
        elif transaction_type == "expense":
            data["expenses"].append({"amount": amount, "description": description})
            data["balance"] -= amount

        return redirect(url_for("index"))

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
