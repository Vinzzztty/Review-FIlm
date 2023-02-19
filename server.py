from flask import Flask, render_template
import datetime
from post import Post
import requests

current_year = datetime.datetime.now().year
posts = requests.get("https://api.npoint.io/91f6a0db516b05456310").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["score"], post["photo"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", year=current_year, all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)