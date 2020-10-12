from nltk import *
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import Counter
from utils import *
from preprocess import pre_process

import math
import numpy as np
import os
import pickle

""" Use the wordnet corpus dataset and return the text representing 
the expanded query """

def expand_query(text):
    text = text.lower()
    tokens = word_tokenize(text)

    #find synonyms to words in the given text

    similar = []

    for word in tokens:
        for syn in wordnet.synsets(word):
            if len(syn.lemmas()) > 3:
                for x in range(3):
                    similar.append(syn.lemmas()[x].name())
            else:
                for x in range(len(syn.lemmas())):
                    similar.append(syn.lemmas()[x].name())
    

    #add the similar words to the query

    for word in similar:
        if word not in text:
            text += " " + word

    return text

""" We can use the expanded query and return each document that is similar
we return required number of search results
We use concepts of cosine-similarity to find the following """

def query(query, no_of_docs):
    query = expand_query(query)
    query = pre_process(query)

    #read persistant storage

    pickle_in = open('serial.txt', 'rb+')
    db = pickle.load(pickle_in)
    pickle_in.close()

    #get data that we stored in the map

    words = db['words']
    N = db['N']
    documents_vector = db['documents_vector']
    dfs = db['dfs']

    #generate query vector

    query_vector = []

    for word in words:
        #calculate document frequency
        tf = 0
        for term in query:
            if term == word:
                tf = tf + 1

        df = 1 if dfs[word] == 0 else dfs[word]

        idf = math.log(N/df)
        tfidf = tf*idf
        query_vector.append(tfidf)

    
    #calculate cosine similarity 
    
    scores = []
    for vector in documents_vector:
        score = np.dot(vector, query_vector)
        scores.append(score)

    document_scores = []

    dir = r'C:\Users\Arabella\Documents\pyspace\probs'
    file_dir = os.listdir(dir)
    file_dir.sort()

    for x in range(len(file_dir)):
        document_scores.append((scores[x], file_dir[x]))

    document_scores.sort(reverse=True)

    #return no_of_docs documents
    result = []

    if len(document_scores) < no_of_docs:
        for x in range(len(document_scores)):
            result.append(document_scores[x])
    else:
        for x in range(no_of_docs):
            result.append(document_scores[x])

    return result

