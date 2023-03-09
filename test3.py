import feedparser
from flask import Flask, render_template, request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer


app = Flask(__name__)

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

        # summarize the article using TextRank
        parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document,sentences_count=2)

        # concatenate the summary sentences with a period
        summary_text = ''
        for sentence in summary:
            summary_text += str(sentence) + '. '

        # remove any special characters from the summary
        summary_text = re.sub(r'[^\w\s.]', '', summary_text)
    except:
        summary_text = ''
    return summary_text




def parse_feed(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        if 'title' in entry and 'link' in entry:
            summary = get_summary(entry.link)
            if summary and len(summary.split()) >= 15: # check if summary is not empty and has at least 15 words
                articles.append({
                    "title": entry.title,
                    "url": entry.link,
                    "summary": summary
                })
            elif not summary:
                continue
        if len(articles) == 6:
            break
    while len(articles) < 6:
        articles.append({
            "title": "No article available",
            "url": "",
            "summary": ""
        })
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
