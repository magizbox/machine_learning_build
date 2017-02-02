#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from collections import Counter
from time import time

sys.path.append("./tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess(words_file="./tools/word_data.pkl", authors_file="./tools/email_authors.pkl")
# features_train = features_train[:len(features_train) / 10]
# labels_train = labels_train[:len(labels_train) / 10]

clf = SVC(kernel='rbf', C=10)
t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")
t0 = time()
print("accuracy:", clf.score(features_test, labels_test))
print("accuracy time:", round(time() - t0, 3), "s")

pred = clf.predict(features_test)

print "Predictions:"
print "10:", pred[10]
print "26:", pred[26]
print "50:", pred[50]

c = Counter(pred)
print c
print "No of predictions for Chris(1):", c[1]
