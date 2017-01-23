# -*- coding: utf-8 -*-
from gensim import corpora
from gensim.matutils import *
from sklearn.feature_extraction import *
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import *
from collections import namedtuple
import os

def load_dataset(data_folder):
    folders = os.listdir(data_folder)
    files = []
    y = []
    for folder in folders:
        path = os.path.join(data_folder, folder)
        current_files = [os.path.join(path, filename) for filename in os.listdir(path)]
        files += current_files
        y += [folder] * len(current_files)
    documents = [open(file, "r").read() for file in files]
    vectorizer = CountVectorizer(min_df=1, ngram_range=(1, 2))
    X = vectorizer.fit_transform(documents).toarray()
    Dataset = namedtuple('Dataset', 'data target')
    dataset = Dataset(data=X, target=y)
    return dataset

# load dataset
data_folder = u"data"
poet = load_dataset(data_folder)
x_train, x_test, y_train, y_test = train_test_split(poet.data, poet.target, test_size=0.2)
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(x_train, y_train)
print clf.score(x_test, y_test)
