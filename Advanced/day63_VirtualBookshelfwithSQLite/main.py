from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# ----------------------- DB Setup --------------------- #
# create the app
app = Flask(__name__)
# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


# Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create initial database
# with app.app_context():
#     db.create_all()

# ----------------------- Web Setup --------------------- #
@app.route('/')
def home():

    with app.app_context():
        all_books = db.session.query(Book).all()
    return render_template('index.html', num=len(all_books), books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['name'],
            author=request.form['author'],
            rating=request.form['rate']
        )
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
    return render_template('add.html')


@app.route("/edit<int:num>", methods=['GET', 'POST'])
def edit(num, methods=['GET', 'POST']):
    if request.method == 'POST':
        new_rating = request.form['rating']
        with app.app_context():
            book_id = num
            book_to_update = Book.query.get(book_id)
            # Cathe not input error
            try:
                book_to_update.rating = new_rating
                db.session.commit()
            except:
                pass
        return redirect(url_for('home'))
    target_book = Book.query.filter_by(id=num).first()
    return render_template('edit.html', book=target_book)


@app.route("/delete<int:num>", methods=['GET', 'POST'])
def delete(num):
    with app.app_context():
        book_id = num
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

