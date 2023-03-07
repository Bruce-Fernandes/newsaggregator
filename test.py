from flask import Flask, render_template
import newspaper

app = Flask(__name__)

@app.route("/")
def home():
    indiatodaypaper = newspaper.build("https://www.indiatoday.in/technology/news", memoize_articles=False, language="en")
    articles = []
    for article in indiatodaypaper.articles[:3]:
        article.download()
        article.parse()
        article.nlp()
        articles.append({
            "title": article.title,
            "url": article.url,
            "summary": article.summary
        })
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
