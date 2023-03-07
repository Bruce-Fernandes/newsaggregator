import time
import feedparser
from flask import Flask, render_template, request

app = Flask(__name__)
def get_feed_urls(query):
    urls = []
    url = f"https://news.google.com/search?q={query}&hl=en-US&gl=IN&ceid=IN%3Aen"
    urls.append(url)
    return urls


def parse_feed(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        if 'title' in entry and 'link' in entry:
            articles.append({
                "title": entry.title,
                "url": entry.link,
                "summary": ""
            })
        if len(articles) == 6:
            break
    return articles

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        feed_urls = get_feed_urls(query)
    else:
        query = "AI"  # default search query
        feed_urls = get_feed_urls(query)

    articles = []
    for url in feed_urls:
        articles += parse_feed(url)
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
