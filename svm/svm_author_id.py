#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.svm import SVC
import time
import numpy

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel='rbf', C=10000.0)
start = time.time()
clf.fit(features_train, labels_train)
end = time.time()
print(end - start)

start = time.time()
labels_pred = clf.predict(features_test)
end = time.time()
print(end - start)

print "10 ->", labels_pred[10]
print "26 ->", labels_pred[26]
print "50 ->", labels_pred[50]

print "Chris ->",list(labels_pred).count(1)

from sklearn.metrics import accuracy_score
print accuracy_score(labels_test, labels_pred)

#########################################################
### your code goes here ###

#########################################################


