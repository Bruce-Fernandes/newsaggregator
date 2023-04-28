import parsefeed
from flask import Flask, render_template, request, redirect, url_for
import geturls
import pyrebase
import loginfunction
import firebaseconfig
import requests

def signup(e, passw):
    firebase = pyrebase.initialize_app(firebaseconfig.firebase_config)
    auth = firebase.auth()
    email = e
    password = passw
    ur = auth.create_user_with_email_and_password(email, password)


app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')
        l = loginfunction.loginF(email, password)
        return l
    return render_template("login.html")


@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        signup(email, password2)
        return redirect(url_for('login'))

    return render_template("sign_up.html")


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        feed_urls = geturls.get_feed_urls(query)
    else:
        query = "Technology"  # default search query
        feed_urls = geturls.get_feed_urls(query)

    articles = []
    for url in feed_urls:
        response=requests.get(url)
        actualurl=response.url
        articles += parsefeed.parse_feed(actualurl)
        if len(articles) >= 8:
            break

    unique_articles = []
    for article in articles:
        if article not in unique_articles:
            unique_articles.append(article)

    while len(unique_articles) < 6:
        unique_articles.append({
            "title": "No article available",
            "url": "",
            "summary": ""
        })

    return render_template("index.html", articles=unique_articles, query=query)


@app.route("/login-page", methods=['GET'])
def login_page():
    return render_template("login.html")


@app.route("/dashboard-page",methods=['GET'])
def dashboard_page():
    return render_template("dashboard.html")

@app.route("/signup-page", methods=['GET'])
def signup_page():
    return render_template("sign_up.html")


if __name__ == "__main__":
    app.run(debug=True)
