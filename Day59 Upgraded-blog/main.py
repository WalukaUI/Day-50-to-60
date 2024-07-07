from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    res = requests.get("https://api.npoint.io/80e17894fb83a9e27424").json()
    return render_template("index.html", jsons=res)


@app.route("/contact")
def get_contacts():
    return render_template("contact.html")


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/post/<id_num>")
def get_post(id_num):
    res = requests.get(f"https://api.npoint.io/80e17894fb83a9e27424/{int(id_num)}").json()
    print(res)
    return render_template("post.html")


if __name__ == "__main__":
   app.run(debug=True)