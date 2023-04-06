import parsefeed
from flask import Flask, render_template, request
import geturls
import pyrebase
import firebaseconfig
def loginF(e, passw):
    firebase = pyrebase.initialize_app(firebaseconfig.firebase_config)
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

    