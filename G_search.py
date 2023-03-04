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
    for url in results[:3]:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        article.nlp()
        articles.append({
            "title": article.title,
            "url": article.url,
            "summary": article.summary
        })
    return render_template("indexxx.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
