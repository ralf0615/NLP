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
