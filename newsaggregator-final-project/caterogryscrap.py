import newspaper

indiatodaypaper=newspaper.build("https://www.indiatoday.in/technology/news",memoize_articles=False,language="en")
# article=Article(url="https://www.indiatoday.in/technology/news/story/ai-taking-over-human-jobs-survey-reveals-chatgpt-has-started-replacing-humans-in-the-workplace-2340552-2023-02-28",language='en')

# first_article=indiatodaypaper.articles[0]
# second_article=indiatodaypaper.articles[1]
# third_article=indiatodaypaper.articles[2]

i=0
while(i<3):
   print( indiatodaypaper._get_category_urls())