from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# ------- Create app--------#
app = Flask(__name__)

# ------- Connect to database --------#
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


# ------- Create table --------#
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# # ------- initial database --------#
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    print(type(all_books))
    return render_template('index.html', num=len(all_books), books=all_books)


@app.route("/edit<int:id>", methods=['GET', 'POST'])
def edit(id):
    book_to_edit = Book.query.get(id)
    if request.method == 'POST':
        book_to_edit.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book_to_edit)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating'],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/delete<int:id>", methods=['GET', 'POST'])
def delete(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

