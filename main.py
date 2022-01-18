from flask import Flask, render_template
from datetime import datetime
import requests
import random

app = Flask(__name__)


def get_gender(name):
    response = requests.get("https://api.genderize.io?name=" + name).json()
    gender = response.get("gender")
    prob = response.get("probability")
    return gender, prob


def get_age(name):
    response = requests.get("https://api.agify.io?name=" + name).json()
    return response.get("age")


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", random_nbr=random_number,
                           copy_year=datetime.now().year)


@app.route("/guess/<name>")
def guess_page(name):
    name = name.capitalize()
    gender, prob = get_gender(name)
    age = get_age(name)
    return render_template("guess.html", name=name, gender=gender, prob=prob, age=age)


@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
