import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def post_data():
    name = request.form["fname"]
    pw = request.form["pword"]
    return f"<h1>name : {name}, pw : {pw}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
