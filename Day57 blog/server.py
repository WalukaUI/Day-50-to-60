from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/<name>")
def hello_name(name):
    ages = requests.get(f"https://api.agify.io/?name={name}")
    res = ages.json()
    return render_template("index.html", name=name, age=res["age"])


if __name__ == "__main__":
    app.run(debug=True)
