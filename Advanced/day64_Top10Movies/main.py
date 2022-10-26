from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

API_KEY = os.environ.get('TMDB_KRY')
SEARCH_ENDPOINT = 'https://api.themoviedb.org/3/search/movie'
DETAIL_ENDPOINT = 'https://api.themoviedb.org/3/movie'

# ------------------Create App------------------#
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# ------------------Create DB------------------#
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movie-collection"
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(5000))
    img_url = db.Column(db.String(250), nullable=False)


# with app.app_context():
#     db.create_all()


# ------------------Create WTForm------------------#
class EditForm(FlaskForm):
    rating = FloatField(label='Your Rating out of 10, e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


# ------------------Web Set------------------#
@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
        db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/delete<int:num>", methods=['GET', 'POST'])
def delete(num):
    movie_id = num
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_form = AddForm(meta={'csrf': False})
    if add_form.validate_on_submit():
        movie_name = add_form.title.data
        params = {
            'api_key': API_KEY,
            'query': movie_name,
        }
        response = requests.get(SEARCH_ENDPOINT, params=params)
        response.raise_for_status()
        search_data = response.json()['results']
        return render_template('select.html', results=search_data)

    return render_template("add.html", form=add_form)


@app.route("/edit<int:num>", methods=['GET', 'POST'])
def edit(num):
    edit_form = EditForm(meta={'csrf': False})
    movie_to_update = Movie.query.get(num)
    if edit_form.validate_on_submit():
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", title=movie_to_update.title, form=edit_form)


@app.route("/select<int:m_id>", methods=['GET', 'POST'])
def selected(m_id):
    params = {
        'api_key': API_KEY,
    }
    response = requests.get(f'{DETAIL_ENDPOINT}/{m_id}', params=params)
    response.raise_for_status()
    detail = response.json()
    new_movie = Movie(title=detail['original_title'],
                      year=detail['release_date'].split('-')[0],
                      description=detail['overview'],
                      img_url=f'https://image.tmdb.org/t/p/original{detail["poster_path"]}',
                      rating=0, ranking=0, review='pass',
                      )
    db.session.add(new_movie)
    db.session.commit()
    movie_to_update = Movie.query.filter_by(title=detail['original_title']).first()
    return redirect(url_for('edit', num=movie_to_update.id))


if __name__ == '__main__':
    app.run(debug=True)
