from flask import Flask, render_template
import feedparser

app = Flask(__name__)

RSS_FEEDS = {
    'techcrunch': 'https://techcrunch.com/feed/',
    'wired': 'https://www.wired.com/feed/rss',
    'verge': 'https://www.theverge.com/rss/index.xml'
}

@app.route("/")
def get_news():
    articles = []
    for feed in RSS_FEEDS.values():
        feed_articles = feedparser.parse(feed)['entries']
        articles.extend(feed_articles)
    sorted_articles = sorted(articles, key=lambda k: k['published_parsed'], reverse=True)
    return render_template('index.html', articles=sorted_articles)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
