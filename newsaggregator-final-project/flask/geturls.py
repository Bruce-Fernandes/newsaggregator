from urllib.parse import urlencode
def get_feed_urls(query):
    modquery="technology news related to"+query

    urls = []
    base_url = "https://news.google.com"
    params = {
        "q":  query,
        "hl": "en-US",
        "gl": "US",
        "ceid": "US:en"
    }
    url = base_url + "/rss/search?" + urlencode(params)
    urls.append(url)
    return urls
# import urllib.parse

# def get_feed_urls(query):
#     urls = []
#     base_url = "https://news.google.com"
#     params = {
#         "q": query,
#         "hl": "en-US",
#         "gl": "US",
#         "ceid": "US:en"
#     }
#     encoded_query = urllib.parse.quote(query)
#     url = f"{base_url}/topics/{encoded_query}?" + urllib.parse.urlencode(params)
#     urls.append(url)
#     return urls

    