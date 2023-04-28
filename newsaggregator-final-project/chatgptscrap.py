import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Replace "article_url" with the actual URL of the news article you want to summarize
article_url = "https://www.indiatoday.in/technology/news/story/redmi-unveils-300w-fast-charging-tech-fully-charge-xiaomi-phone-under-5-minutes-2340988-2023-03-01"

# Get the HTML content of the article using requests
response = requests.get(article_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the text content of the article
article_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))

# Tokenize the article text into words and sentences
stop_words = set(stopwords.words("english"))
words = word_tokenize(article_text)
sentences = sent_tokenize(article_text)

# Calculate the word frequency of the article
word_frequencies = {}
for word in words:
    if word.lower() not in stop_words:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

# Calculate the sentence score of the article based on word frequency
sentence_scores = {}
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_frequencies:
            if len(sentence.split(" ")) < 30:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]

# Get the top 3 sentences with the highest score
summary_sentences = sorted(
    sentence_scores, key=sentence_scores.get, reverse=True)[:3]

# Print the summary of the article
print(" ".join(summary_sentences))
