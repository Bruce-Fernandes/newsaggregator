import urllib.parse


def get_feed_urls(query):
    urls = []
    url = "https://news.google.com/search?q={}&hl=en-US&gl=IN&ceid=IN%3Aen".format(urllib.parse.quote(query))
    urls.append(url)
    print(urls)

query = input("Enter your search query: ")
get_feed_urls(query)

# import urllib.parse
# import newspaper

# def get_feed_urls(query):
#     urls = []
#     url = "https://news.google.com/search?q={}&hl=en-US&gl=IN&ceid=IN%3Aen".format(urllib.parse.quote(query))
#     urls.append(url)
#     for url in urls:
#         print(url)
    
#     # Loop through search result pages and extract article URLs
#     article_urls = []
#     for url in urls[:5]:
#         search_page = newspaper.build(url)
#         article_urls.extend(search_page.article_urls())
    
#     # Loop through article URLs and extract title and summary of each article
#     for article_url in article_urls:
#         try:
#             article = newspaper.Article(article_url)
#             article.download()
#             article.parse()
#             title = article.title
#             summary = article.summary
#             print("Title:", title)
#             print("Summary:", summary)
#         except:
#             print("Error while extracting article from:", article_url)

# query = input("Enter your search query: ")
# get_feed_urls(query)


