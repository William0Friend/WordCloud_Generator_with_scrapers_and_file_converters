from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

with open("clean_full.txt", "r", encoding='utf-8', errors='ignore') as f:
   

   def create_wordcloud(text):
      #mask = np.array(Image.open(os.path.join(currdir, "cloud.png")))
      mask = np.array((Image.open('cloud.png')))
      stopwords = set(STOPWORDS)
      stopwords.add('will')
      stopwords.add('really')
      stopwords.add('http')
      stopwords.add('good')
      stopwords.add('got')
      stopwords.add('great')
      stopwords.add('ve')
      stopwords.add('put')
      stopwords.add('first')
      stopwords.add('say')
      stopwords.add('many')
      stopwords.add('made')
      stopwords.add('don')
      stopwords.add('something')
      stopwords.add('though')
      stopwords.add('bad')
      stopwords.add('ll')
      stopwords.add('https')
      stopwords.add('new')
      stopwords.add('hard')
      stopwords.add('see')
      stopwords.add('make')
      stopwords.add('little')
      stopwords.add('said')
      stopwords.add('sci')
      stopwords.add('thing')
      stopwords.add('re')
      stopwords.add('one')
      stopwords.add('didn')
      stopwords.add('part')
      stopwords.add('may')
      stopwords.add('come')
      stopwords.add('week')
      stopwords.add('sure')
      stopwords.add('tell')
      stopwords.add('seem')
      stopwords.add('way')
      stopwords.add('lot')
      stopwords.add('bit')
      stopwords.add('look')
      stopwords.add('take')
      stopwords.add('every')
      stopwords.add('another')
      stopwords.add('probably')
      stopwords.add('doesn')
      stopwords.add('took')
      stopwords.add('actually')
      stopwords.add('hour')
      stopwords.add('using')
      stopwords.add('much')
      stopwords.add('getting')
      stopwords.add('went')
      stopwords.add('month')
      stopwords.add('things')
      stopwords.add('place')
      stopwords.add('definitely')
      stopwords.add('months')
      stopwords.add('might')
      #stopwords.add('maybe')
      #stopwords.add('everyone')
      #stopwords.add('without')
      #stopwords.add('want')


      wc = WordCloud(background_color='black',
                     mask=mask,
                     max_words = 100,
                     stopwords=stopwords)
      wc.generate(text)
      wc.to_file("wcc_8_full_black.png")
   print('Was f opened for reading: ' , f.readable())
   create_wordcloud(f.read())










"""
def create_word_cloud(string):
   maskArray = npy.array(Image.open("cloud.jpg"))
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.png")

dataset = dataset.lower()
create_word_cloud(dataset)

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
    #mask = np.array(Image.open(os.path.join(currdir, "cloud.png")))
    mask = np.array((Image.open('cloud.png')))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color='white',
                    mask=mask,
                    max_words = 200,
                    stopwords=stopwords)
    wc.generate(text)
    wc.to_file("wc.png")

create_wordcloud(get_wiki("python programming language"))
"""