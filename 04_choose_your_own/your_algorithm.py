#!/usr/bin/python
from time import time

import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################




def optimize_params():
    max_accuracy = 0
    for i in range(4, 100, 1):
        print i
        clf = RandomForestClassifier(n_estimators=10, min_samples_split=i)
        t0 = time()
        clf.fit(features_train, labels_train)
        print("training time:", round(time() - t0, 3), "s")
        accuracy = clf.score(features_test, labels_test)
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            print("accuracy:", accuracy, "(BEST)")
        else:
            print("accuracy:", accuracy)


def best_model():
    KNeighborsClassifier
    clf = KNeighborsClassifier(algorithm='brute',n_neighbors=18)

    # AdaBoostClassifier
    # optimized_estimators = 20
    # optimized_learning_rate = 2
    # clf = AdaBoostClassifier(n_estimators=optimized_estimators, learning_rate=optimized_learning_rate)

    # RandomForest
    # optimized_n_estimators = 10
    # optimized_min_samples_split = 36
    # clf = RandomForestClassifier(
    #     n_estimators=optimized_n_estimators,
    #     min_samples_split=optimized_min_samples_split)

    t0 = time()
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    print("training time:", round(time() - t0, 3), "s")
    accuracy = clf.score(features_test, labels_test)
    target_names = ['fast', 'slow']
    print(classification_report(labels_test, pred, target_names=target_names))
    print("accuracy:", accuracy)
    try:
        prettyPicture(clf, features_test, labels_test)
    except Exception, error:
        raise error


# optimize_params()
best_model()
