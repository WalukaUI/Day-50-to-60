from flask import Flask, render_template
from file import jsons
from post import Post


post_objects = []
for post in jsons:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
print(post_objects)

app = Flask(__name__)

@app.route('/')
def home():
    print(post_objects)
    return render_template("index.html", all_posts=post_objects)


if __name__ == "__main__":
    app.run(debug=True)
