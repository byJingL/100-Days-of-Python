from flask import Flask, render_template
import random
from datetime import datetime
import requests
GENDER_ENDPOINT = 'https://api.genderize.io?name='
AGE_ENDPOINT = 'https://api.agify.io?name='
BLOG_ENDPOINT = 'https://api.npoint.io/868b72e1a04a5450f98d'
app = Flask(__name__)


def get_name_gender(name):
    response = requests.get(f'{GENDER_ENDPOINT}{name}')
    response.raise_for_status()
    gender = response.json()["gender"]
    return gender


def get_name_age(name):
    response = requests.get(f'{AGE_ENDPOINT}{name}')
    response.raise_for_status()
    age = response.json()["age"]
    return age


@app.route('/')
def homepage():
    random_num = random.randint(1, 20)
    current_year = datetime.now().year
    return render_template('index.html', num=random_num, year=current_year)


@app.route('/guess/<string:name>')
def name_detective(name):
    name_gender = get_name_gender(name)
    name_age = get_name_age(name)
    return render_template('name.html', name=name, gender=name_gender, age=name_age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get(BLOG_ENDPOINT)
    response.raise_for_status()
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)



if __name__ == '__main__':
    app.run(debug=True)
