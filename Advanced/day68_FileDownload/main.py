from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user


# ------------------ Create APP------------------#
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
# login module
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# ------------------ Create DB------------------#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create table in DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# with app.app_context():
#     db.create_all()


# ------------------ Web Set------------------#
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        if User.query.filter_by(email=email).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hashed_salted_password = generate_password_hash(
            password=request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8)

        new_user = User(
            email=email,
            password=hashed_salted_password,
            name=request.form.get('name'),
        )
        db.session.add(new_user)
        db.session.commit()
        # log in new user
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_password = request.form.get('password')
        user_to_login = User.query.filter_by(email=user_email).first()

        if not user_to_login:
            flash("This email doesn't exist, please try again")
            return redirect(url_for('login'))
        # Check stored password hash against entered password hashed.
        elif not check_password_hash(user_to_login.password, user_password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user_to_login)
            return redirect(url_for('secrets'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    print(current_user)
    return render_template("secrets.html", username=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/download', methods=['GET', 'POST'])
@login_required
def download():
    return send_from_directory(directory='static', path='files/cheat_sheet.pdf', as_attachment=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
