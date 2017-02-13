#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    cleaned_data = zip(ages[:,0], net_worths[:,0], [x - y for x, y in zip(predictions[:,0], net_worths[:,0])])

    cleaned_data = sorted(cleaned_data, key=lambda p: p[2])

    print cleaned_data[0]
    print cleaned_data[len(cleaned_data) -1]
    print len(cleaned_data) * 0.9
    return cleaned_data[0:int(len(cleaned_data) * .9)]

