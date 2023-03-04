from googlesearch import search 
from flask import Flask, render_template, request
import newspaper


app = Flask(__name__)

def google_search(query):
    results = search(query, num_results=10 )
    return results

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results = google_search(query)
    else:
        query = "Python"  # default search query
        results = google_search(query)

    articles = []
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

    return render_template("index.html", articles=articles, query=query)

if __name__ == "__main__":
    app.run(debug=True)