from newspaper import Article
import newspaper


indiatodaypaper=newspaper.build("https://www.indiatoday.in/technology/news",memoize_articles=False,language="en")
# article=Article(url="https://www.indiatoday.in/technology/news/story/ai-taking-over-human-jobs-survey-reveals-chatgpt-has-started-replacing-humans-in-the-workplace-2340552-2023-02-28",language='en')
artarray=[]
counter=0
for article in indiatodaypaper.articles:
    counter=counter+1
    if(counter>3):
        break
    artarray.append(article.url)
print(artarray)
# # print(indiatodaypaper.size())
# for catergory in indiatodaypaper.category_urls():
#     print(catergory)


for i in artarray :

    artarray.download()
    artarray.parse()
    artarray.nlp()
    # print(article.summary)
    print("Article title:",artarray.title)