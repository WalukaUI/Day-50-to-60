from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/posts")
def hello_world():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return render_template("blogs.html", all_posts=posts)


@app.route("/guess/<name>")
def hello_name(name):
    ages = requests.get(f"https://api.agify.io/?name={name}")
    res = ages.json()
    return render_template("index.html", name=name, age=res["age"])


if __name__ == "__main__":
    app.run(debug=True)
