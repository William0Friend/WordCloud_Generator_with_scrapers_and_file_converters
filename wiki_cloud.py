import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np

#currdir = os.path.dirname(__file__)
def get_wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

def create_wordcloud(text):
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color='white',
                    mask=mask,
                    max_words = 200,
                    stopwords=stopwords)
    wc.generate(text)
    wc.to_file("wc.png")

create_wordcloud(get_wiki("python programming language"))