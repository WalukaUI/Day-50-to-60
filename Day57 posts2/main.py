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
    return render_template("index.html", all_posts=post_objects)


@app.route("/<int:index>")
def get_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    print(requested_post)
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
