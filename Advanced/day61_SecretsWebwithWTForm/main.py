from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_bootstrap import Bootstrap

DEFAULT_EMAIL = 'admin@email.com'
DEFAULT_PASS = '12345678'


def password_length_check(form, field):
    if len(field.data) < 8:
        raise ValidationError('Password must be at least 8 characters')


# 'email''password''submit' are form field
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), password_length_check])
    submit = SubmitField(label='Log In')


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


app = create_app()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    print("call it")
    login_form = LoginForm(meta={'csrf': False})
    if login_form.validate_on_submit():
        if login_form.email.data == DEFAULT_EMAIL and login_form.password.data == DEFAULT_PASS:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
