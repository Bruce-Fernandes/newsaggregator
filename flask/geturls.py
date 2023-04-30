from urllib.parse import urlencode
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