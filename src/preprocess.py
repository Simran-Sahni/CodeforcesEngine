from nltk import word_tokenize, PorterStemmer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import Counter
import string
import nltk

""" Takes a text as string 
Performs operations like tokenizations, stemming, and removes stopwords
returns an array of strings with words that have significance """

def pre_process(text):
    text = text.lower()

    #tokenization
    text = text.translate(str.maketrans("","", string.punctuation))
    tokens = word_tokenize(text)


    #filter out the stopwords

    stop_words = set(stopwords.words('english'))
    words_filtered = []


    for word in tokens:
        if word not in stop_words:
            words_filtered.append(word)

    #Perform stemming

    words_stemmed = []

    ps = PorterStemmer()

    for word in words_filtered:
        if(word.isalpha() or word.isnumeric()):
            words_stemmed.append(ps.stem(word))

    return words_stemmed

