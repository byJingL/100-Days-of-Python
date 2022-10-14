from flask import Flask, render_template
import requests
BLOG_ENDPOINT = 'https://api.npoint.io/868b72e1a04a5450f98d'

app = Flask(__name__)
response = requests.get(BLOG_ENDPOINT)
response.raise_for_status()
all_posts = response.json()
all_blogs = [post for post in all_posts]


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


# # Very important!: <int:num>, if not, num is a string
# @app.route('/blog/<int:num>')
# def get_post(num):
#     print(num)
#     return render_template("post.html", blog_id=num, blogs=all_posts)


# Other Solution: Simple and put for,if in main.py
@app.route('/blog/<int:num>')
def get_post(num):
    print(num)
    blog_to_display = all_blogs[num-1]
    print(blog_to_display)
    return render_template("post.html", blog=blog_to_display)


if __name__ == "__main__":
    app.run(debug=True)
