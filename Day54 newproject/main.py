from flask import Flask

app = Flask(__name__)


def make_bold(fn):
    def wrapper():
        return f'<b>{fn()}</b>'
    return wrapper


def make_italic(fn):
    def wrapper():
        return f'<i>{fn()}</i>'
    return wrapper


@app.route("/bye")
@make_bold
@make_italic
def hello_world():
    return "Hello, World! fghjfgjgfjgfjgfjgfjgf"

@app.route("/name")
def hello_name():
    return "name is name"


@app.route("/username/<name>/<int:number>")
def bye(name, number):
    return f"helloooooohhhh {name}, number is {number}"


if __name__ == "__main__":
    app.run(debug=True)

