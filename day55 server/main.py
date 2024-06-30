from flask import Flask
import random
app = Flask(__name__)


rand_num = random.randrange(0,9)
@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center' >Guess aa number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='anime'>")

@app.route("/<int:num>")
def num_test(num):
    if num > rand_num:
        return "<h1 style='color: red'>Too High, Try again.......</h1>"
    elif num < rand_num:
        return "<h1 style='color: blue'>Too low, Try again.......</h1>"
    else:
        return "<h1 style='color: green'>Wooo Correct.......</h1>"


if __name__ == "__main__":
    app.run(debug=True)