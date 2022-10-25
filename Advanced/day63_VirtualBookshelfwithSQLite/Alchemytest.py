from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
# initialize the app with the extension
db.init_app(app)


# Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create initial database
with app.app_context():
    db.create_all()


# Create new record
# new_book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=6.8)
# with app.app_context():
#     db.session.add(new_book)
#     db.session.commit()

# new_book = Book(title='Why Be Happy When You Could Be Normal?', author='Jeanette Winterson', rating=10)
# with app.app_context():
#     db.session.add(new_book)
#     db.session.commit()

# new_book = Book(title='Oranges Are Not the Only Fruit', author='Jeanette Winterson', rating=9)
# with app.app_context():
#     db.session.add(new_book)
#     db.session.commit()

# new_book = Book(title='The Gap of Time', author='Jeanette Winterson', rating=8.8)
# with app.app_context():
#     db.session.add(new_book)
#     db.session.commit()

# Read all records and a particular record
with app.app_context():
    all_books = db.session.query(Book).all()
    print(all_books)

    hp = db.session.execute(db.select(Book).filter_by(author="Jeanette Winterson"))
    print(hp)

    jw = Book.query.filter_by(author="Jeanette Winterson").first()
    print(jw)

# Update the record
with app.app_context():
    # A Particular Record By Query
    book_to_update = Book.query.filter_by(id=1).first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()
    # A Record By PRIMARY KEY
    book_id = 1
    book_to_update = Book.query.get(book_id)
    book_to_update.rating = 6.5
    db.session.commit()

# Delete the record: A Particular Record By PRIMARY KEY
# with app.app_context():
#     book_id = 1
#     book_to_delete = Book.query.get(book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
