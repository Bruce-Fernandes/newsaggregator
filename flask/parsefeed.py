import feedparser
import getsummary



def parse_feed(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        if 'title' in entry and 'link' in entry:
            summary = getsummary.get_summary(entry.link)
            if summary and len(summary.split()) >= 15: # check if summary is not empty and has at least 15 words
                articles.append({
                    "title": entry.title,
                    "url": entry.link,
                    "summary": summary
                })
            elif not summary:
                continue
        if len(articles) == 8:
            break
    while len(articles) < 8:
        articles.append({
            "title": "No article available",
            "url": "",
            "summary": ""
        })
    return articles