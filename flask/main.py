import parsefeed
from flask import Flask, render_template, request
import geturls

app = Flask(__name__)

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