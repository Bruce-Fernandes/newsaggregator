import feedparser
import newspaper


def parse_feed(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        if 'title' in entry and 'link' in entry:
            try:
                article = newspaper.Article(entry.link)
                article.download()
                article.parse()
                article.nlp()
                if article.summary and len(article.summary.split()) >= 15:
                    articles.append({
                        "title": entry.title,
                        "url": entry.link,
                        "summary": article.summary,
                        "image": article.top_image
                    })
            except newspaper.article.ArticleException:
                # Skip this article if there's an exception
                continue
        if len(articles) == 8:
            break
    while len(articles) < 8:
        articles.append({
            "title": "No article available",
            "url": "",
            "summary": "",
            "image": ""
        })
    return articles
