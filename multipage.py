
import newspaper

indiatodaypaper=newspaper.build("https://www.indiatoday.in/technology/news",memoize_articles=False,language="en")
i=0
while(i<3):
    indiatodaypaper.articles[i].download()
    indiatodaypaper.articles[i].parse()
    indiatodaypaper.articles[i].nlp()
    print("Title :  ",indiatodaypaper.articles[i].title)
    print()
    print("URL:  ",indiatodaypaper.articles[i].url)
    print()
    print("Summary :  ",indiatodaypaper.articles[i].summary)
    print()
    i=i+1
    print()
    print()
    print()
# first_article.download()
# first_article.parse()
# first_article.nlp()
# print(first_article.title)
   