from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! fghjfgjgfjgfjgfjgfjgf"


@app.route("/username/<name>/<int:number>")
def bye(name, number):
    return f"helloooooohhh {name}, number is {number}"


if __name__ == "__main__":
    app.run(debug=True)

