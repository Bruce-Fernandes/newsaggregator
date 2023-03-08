import feedparser
from flask import Flask, render_template, request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
import re
import nltk
from nltk.tokenize import sent_tokenize

app = Flask(__name__)

nltk.download('punkt')

def get_feed_urls(query):
    urls = []
    base_url = "https://news.google.com"
    params = {
        "q": query,
        "hl": "en-US",
        "gl": "US",
        "ceid": "US:en"
    }
    url = base_url + "/rss/search?" + urlencode(params)
    urls.append(url)
    return urls

def get_summary(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # get the main content of the article
        article_text = ''
        for p in soup.find_all('p'):
            article_text += p.get_text()
        # tokenize the article text into sentences and select the first 3
        # sentences as the summary
        sentences = sent_tokenize(article_text)
        summary = ' '.join(sentences[:3])
        # remove any special characters from the summary
        summary = re.sub(r'[^\w\s]','',summary)
    except:
        summary = ''
    return summary

def parse_feed(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        if 'title' in entry and 'link' in entry:
            summary = get_summary(entry.link)
            articles.append({
                "title": entry.title,
                "url": entry.link,
                "summary": summary
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
