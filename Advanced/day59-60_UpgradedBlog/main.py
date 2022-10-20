from flask import Flask, render_template, request
import requests
import smtplib
import os

BLOG_ENDPOINT = 'https://api.npoint.io/868b72e1a04a5450f98d'
MY_EMAIL = os.environ.get()
MY_PASSWORD = os.environ.get()

# ------------------Get blog data------------------#
response = requests.get(BLOG_ENDPOINT)
response.raise_for_status()
posts_data = response.json()
all_posts = [each_post for each_post in posts_data]


# --------------------Send Email---------------------#
def send_mail(name, email, message):
    body = f"Name: {name}\n" \
           f"Email: {email}\n" \
           f"Message: {message}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject: Blog Contact!\n\n{body}")


# ---------------------Set web----------------------#
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=posts_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['visitor']
        email = request.form['email']
        message = request.form['message']
        send_mail(name, email, message)
        return render_template('contact.html', sent_message=True)
    return render_template('contact.html', sent_message=False)


# <int:num> must have, for 'Flask Rooting' Rule
@app.route('/post/<int:num>')
def get_post(num):
    post_to_display = all_posts[num-1]
    return render_template('post.html', post=post_to_display)


if __name__ == "__main__":
    app.run(debug=True)
