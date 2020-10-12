import pickle
import os
import math

from utils import *

from preprocess import pre_process

""" Get all of the documents (problem statements) from /problems/*.txt
returns a list containing all docs """


def get_docs():
    dir = r'C:\Users\Arabella\Documents\pyspace\probs'
    documents = []
    file_dir = os.listdir(dir)
    file_dir.sort()
    for file in file_dir:
        with open(dir + '\\' + file, 'rb') as f:
            cor = f.read()
            documents.append(cor.decode('utf8'))
            f.close()

    return documents


""" 
Calculate tf-idf of all docs together, and store the details in the permanant storage
This is done because we do not have the resources to re-compute everything """

def calculate_tf_idf_docs():

    documents = get_docs()

    #preprocessed documents

    processed_docs = []

    for docs in documents:
        processed_docs.append(pre_process(docs))

    documents = processed_docs

    #extract a list of words in the problems statement

    words = []
    dfs = dict()

    for docs in documents:
        for word in docs:
            if word not in words:
                words.append(word)

    print(len(words))

    for docs in documents:
        tempdfs = set()
        for word in docs:
            tempdfs.add(word)
        for word in tempdfs:
            if not word in dfs:
                dfs[word] = 1
            else:
                dfs[word] = + 1
        


    N = len(documents) + 1
    print(N)
    #generating n-dimensional vectors

    documents_vector = []

    for docs in documents:
        doc_vector = []
        for word in words:
            #for calculating term frequency
            tf = 0
            for term in docs:
                if term == word:
                    tf = tf + 1
            #for calculating document frequency
            idf = math.log(N/dfs[word])

            tf_idf = tf*idf
            doc_vector.append(tf_idf)

        documents_vector.append(doc_vector)

    #making a db
    db = {}
    db['words'] = words
    db['N'] = N
    db['documents_vector'] = documents_vector
    db['dfs'] = dfs

    #save data to storage

    pickle_out = open('serial.txt', 'wb+')
    pickle.dump(db, pickle_out)
    pickle_out.close()

calculate_tf_idf_docs()


