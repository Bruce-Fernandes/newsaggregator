from flask import Flask, render_template
from newspaper import Article

app = Flask(__name__)

def get_summary(url):
    article = Article(url=url, language='en')
    article.download()
    article.parse()
    article.nlp()
    summary = article.summary
    return summary

@app.route('/')
def index():
    url = "https://tech.hindustantimes.com/mobile/iphone-14-just-turned-cheaper-for-you-know-how-to-cut-price-here-check-full-list-71677750949894.html"
    summary = get_summary(url)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
