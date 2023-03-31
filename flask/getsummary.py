from bs4 import BeautifulSoup
import requests
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer

def get_summary(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # get the main content of the article
        article_text = ''
        for p in soup.find_all('p'):
            article_text += p.get_text()

        # summarize the article using TextRank
        parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document,sentences_count=2)

        # concatenate the summary sentences with a period
        summary_text = ''
        for sentence in summary:
            summary_text += str(sentence) + '. '

        # remove any special characters from the summary
        summary_text = re.sub(r'[^\w\s.]', '', summary_text)
    except:
        summary_text = ''
    return summary_text