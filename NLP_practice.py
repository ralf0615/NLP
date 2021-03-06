#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:20:26 2018

@author: yuchenli
@content: NLP
"""

from nltk.book import *
from nltk import *
import nltk as nltk


"""
http://www.nltk.org/book/ch01.html#fig-inaugural
"""
text1

text1.concordance("china")

text1.similar("china")
text2.similar("china")

text2.concordance("monstrous")

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

text3.generate()


"""
1.4 Counting Vocabulary
"""
len(text3)

sorted(set(text3))

text5.count("lol")

"""
3.1 Frequency Distribution
"""
fdist1 = FreqDist(text1)
print(fdist1)
fdist1.most_common(20)


"""
3.3 Collocation and Bigrams
Collocation is a sequence of words that occur together unusually often
"""

"""
5.5 Spoken Dialog Systems
"""
# nltk.chat.chatbots() error

"""
2. Accesing Text Corpora and Lexical Resources
"""

import nltk
nltk.corpus.gutenberg.fileids()

"""
1.8 Text Corpus Structure
"""
sents = gutenberg.sents("burgess-busterbrown.txt")


"""
2.2 Counting Words by Genre
"""
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories = genre))


"""
4. Lexical Resources
"""
my_text = ['My', 'name', 'is', 'Honey', 'Booboo']
vocab = sorted(set(my_text))
word_freq = FreqDist(my_text)

"""
4.1 Wordlist Corpora
"""
from nltk.corpus import stopwords
stopwords.words('english')


"""
5. WordNet
"""
from nltk.corpus import wordnet as wn
wn.synsets('bitch') #just exploring :D
wn.synset('cunt.n.01').lemma_names()
wn.synset('cunt.n.01').definition()

wn.synsets('dish')

for synset in wn.synsets('dish'):
    print(str(synset) + ":" + synset.definition())
    
wn.synset('dish.n.02').definition()

"""
Sematic Similarity
"""
right = wn.synset('right_whale.n.01')


"""
3 Processing Raw Text
"""

from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf-8-sig')
type(raw)
len(raw)
raw[:75]
tokens = word_tokenize(raw)
tokens[:10]

text = nltk.Text(tokens)
text.collocations() #Frequent bigrams

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')
print(html)


from bs4 import BeautifulSoup
raw = BeautifulSoup(html, "lxml").get_text()
tokens = word_tokenize(raw)
tokens

tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')

"""
Reading Local Files
"""
f = open('/Users/yuchenli/Google Drive/Code/Python/NLP/test.txt')
raw = f.read()
f = open('/Users/yuchenli/Google Drive/Code/Python/NLP/test.txt')
f.read()

# Read line by line
f = open('/Users/yuchenli/Google Drive/Code/Python/NLP/test.txt')
for line in f:
    print(line.strip())
    
# Capturing user input
s = input("Enter some text: ")
print("You typed,", len(word_tokenize(s)), "words")

"""
Extracting encoded text from files
"""
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = open(path, encoding = 'latin2')
i=0
for line in f:
    if (i<=5):
        print(line.strip())
        i+=1
        
"""
4 Writing Structured Programs
"""
empty = []
nested = [empty, empty, empty]
nested