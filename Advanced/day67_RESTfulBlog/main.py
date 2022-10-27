from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime
today = datetime.datetime.now().strftime("%B %d,%Y")

# ------------------ Create APP------------------#
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# ------------------ Create DB------------------#
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Configure table
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# with app.app_context():
#     db.create_all()


# ------------------ Create WTForm------------------#
class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


# ------------------ Web Set------------------#
@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=['POST', 'GET'])
def add_post():
    add_form = CreatePostForm()
    if add_form.validate_on_submit():
        new_post = BlogPost(
            title=add_form.title.data,
            subtitle=add_form.subtitle.data,
            date=today,
            body=add_form.body.data,
            author=add_form.author.data,
            img_url=request.form.get('img_url')
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=add_form)


@app.route("/edit-post/<int:post_id>", methods=['POST', 'GET'])
def edit_post(post_id):
    post_to_edit = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        author=post_to_edit.author,
        img_url=post_to_edit.img_url,
        body=post_to_edit.body,
    )
    if edit_form.validate_on_submit():
        post_to_edit.title = edit_form.title.data
        post_to_edit.subtitle = edit_form.subtitle.data
        post_to_edit.author = edit_form.author.data
        post_to_edit.img_url = edit_form.img_url.data
        post_to_edit.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template('make-post.html', form=edit_form, edit=True)


@app.route("/delete/<int:post_id>", methods=['POST', 'GET'])
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
