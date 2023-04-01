import parsefeed
from flask import Flask, render_template, request
import geturls
import pyrebase

firebase_config={

 'apiKey': "AIzaSyC6-waK4BYkZC932vCPCUH__1kMYfgFdcs",
  'authDomain': "newsagg2-80ee1.firebaseapp.com",
  
  'projectId': "newsagg2-80ee1",
  'storageBucket': "newsagg2-80ee1.appspot.com",
  'messagingSenderId': "557250952819",
  'appId': "1:557250952819:web:e1784bbf33193e9fd27406",
  'measurementId': "G-EPDJCJVJ0Q",
  'databaseURL': "https://newsagg2-80ee1-default-rtdb.firebaseio.com"

}

def loginF(e, passw):
    firebase = pyrebase.initialize_app(firebase_config)
    auth = firebase.auth()
    email = e
    password = passw
    try:
        ur = auth.sign_in_with_email_and_password(email, password)
        # if login is successful, get the articles and render the dashboard
        query = "AI"  # default search query
        feed_urls = geturls.get_feed_urls(query)

        articles = []
        for url in feed_urls:
            articles += parsefeed.parse_feed(url)
            if len(articles) >= 6:
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

    except:
        print("Wrong credentials")
        return render_template("login.html")

    

def signup(e,passw):
   
    firebase=pyrebase.initialize_app(firebase_config)
    auth=firebase.auth()
    email=e
    password=passw
    ur=auth.create_user_with_email_and_password(email,password)


app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('username')
        password = request.form.get('password')
        l=loginF(email,password)    
        return l
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        signup(email,password2) 
       
    return render_template("sign_up.html")



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        feed_urls = geturls.get_feed_urls(query)
    else:
        query = "AI"  # default search query
        feed_urls = geturls.get_feed_urls(query)

    articles = []
    for url in feed_urls:
        articles += parsefeed.parse_feed(url)
        if len(articles) >= 6:
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

if __name__ == "__main__":
    app.run(debug=True)