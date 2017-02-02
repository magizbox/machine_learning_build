#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("./tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess(words_file="./tools/word_data.pkl", authors_file="./tools/email_authors.pkl")

# Number of features: 3785
print "Number of features: ", len(features_train[0])

# clf 1
# feature  : percentile=10
# accuracy : 0.978
# time     : 62.838
# clf = DecisionTreeClassifier(min_samples_split=40)
# t0 = time()
# clf.fit(features_train, labels_train)
# print("training time:", round(time() - t0, 3), "s")
# print("accuracy:", clf.score(features_test, labels_test))

# clf 2
# feature  : percentile=1
# accuracy : 0.978
# time     : 4.212
clf = DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")
print("accuracy:", clf.score(features_test, labels_test))
