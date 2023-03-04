from googlesearch import search
from flask import Flask, render_template
import newspaper

app = Flask(__name__)

def google_search(query):
    results = search(query, num_results=10)
    return results

@app.route("/")
def home():
    articles = []
    results = list(google_search("AI news"))
    for url in results:
        try:
            article = newspaper.Article(url)
            article.download()
            article.parse()
            article.nlp()
            articles.append({
                "title": article.title,
                "url": article.url,
                "summary": article.summary
            })
        except newspaper.article.ArticleException:
            continue
        if len(articles) == 3:
            break
    while len(articles) < 3:
        articles.append({
            "title": "No article available",
            "url": "",
            "summary": ""
        })
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
