import newspaper
from newspaper import Article

# indiatodaypaper = newspaper.build(
    # "https://www.indiatoday.in/technology/news", memoize_articles=False, language="en")
article = Article(url="https://www.indiatoday.in/technology/news/story/redmi-unveils-300w-fast-charging-tech-fully-charge-xiaomi-phone-under-5-minutes-2340988-2023-03-01", language='en')
# for article in indiatodaypaper.articles:
#     print(article.url)
# print("size of indiatoday paper is:",indiatodaypaper.size())
# print()
# print()
# for catergory in indiatodaypaper.category_urls():
#     print(catergory)
# print()
# print()
article.download()
article.parse()
article.nlp()
print("Article title:", article.title)
print()
print(article.summary)