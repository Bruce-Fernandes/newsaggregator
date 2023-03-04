from flask import Flask, render_template
import newspaper

app = Flask(__name__)

@app.route('/')
def index():
    # Create a Newspaper object for India Today Technology section
    indiatodaypaper = newspaper.build("https://www.indiatoday.in/technology/news", memoize_articles=False, language="en")
    
    # Download, parse, and perform NLP on the first three articles
    articles = []
    for article in indiatodaypaper.articles[:3]:
        article.download()
        article.parse()
        article.nlp()
        articles.append(article)
    
    # Render the articles on an HTML template
    return render_template('articles.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
