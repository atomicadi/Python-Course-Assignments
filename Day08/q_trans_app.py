# Written by Aditya Barman, Date: June 07, 2026; @weizmann
# calculating translational partition function  

from flask import Flask, render_template, request
from q_trans_logic import calc_q_trans

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        m = request.form["mass"]
        TC = request.form["TC"]
        T = request.form["temperature"]
        V = request.form["volume"]

        result, error = calc_q_trans(m, TC, T, V)

    return render_template(
        "index.html",
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
