from flask import Flask, render_template, request
from logic import calc_q_trans

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        m = request.form["mass"]
        T = request.form["temperature"]
        V = request.form["volume"]

        result, error = calc_q_trans(m, T, V)

    return render_template(
        "index.html",
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
