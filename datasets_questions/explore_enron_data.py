#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print len(enron_data["SKILLING JEFFREY K"])

count1 = 0
count2 = 0
count3 = 0
countPOI = 0
countPOINaN = 0

for key, value in enron_data.iteritems():
    #print key, "corresponds to", value["poi"], "\n"
    if (value["salary"] != 'NaN'):
        count1 += 1
    if (value["email_address"] != 'NaN'):
        count2 += 1
    if (value["total_payments"] == 'NaN'):
        count3 += 1
    if (value["poi"]):
        countPOI += 1
        if (value["total_payments"] == 'NaN'):
            countPOINaN += 1

print "Total Salary:", count1
print "Total Emails:", count2
print "Total NaN Payments:", count3

print "Total NaN Payments POI %:", countPOI

#print enron_data["PRENTICE JAMES"]

#print enron_data["COLWELL WESLEY"]

print enron_data["SKILLING JEFFREY K"]["total_payments"]

print enron_data["FASTOW ANDREW S"]["total_payments"]

print enron_data["LAY KENNETH L"]["total_payments"]

print enron_data["LAY KENNETH L"]

