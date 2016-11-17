# -*- coding: UTF-8 -*-

#A library of functions that compare points with Cartesian coordinates.
#Most useful one checks if the points are collinear, rounding to nearest millionth.

def same_length(list_of_tuples):
    if len(list_of_tuples) <= 1:
        return True
    else:
        length = len(list_of_tuples[0])
        for tup in list_of_tuples:
            if len(tup)!= length:
                return False
        return True

def proportional_pair(pair_of_tuples): #Rounds to nearest a millionth
    assert len(pair_of_tuples) == 2
    assert same_length(pair_of_tuples)
    tup_A = pair_of_tuples[0]
    tup_B = pair_of_tuples[1]
    if len(tup_A)==1:
        return True
    else:
        for i in range(1, len(tup_A)):
            ad = tup_A[i-1]*tup_B[i]
            bc = tup_A[i]*tup_B[i-1]
            if int((10**6)*(ad-bc)) not in [-1, 0, 1]: #rounding performed here
                return False
    return True

def proportional_list(list_of_tuples):
    if len(list_of_tuples) <= 1:
        return True
    assert same_length(list_of_tuples)
    for i in range(1, len(list_of_tuples)):
        if proportional_pair(list_of_tuples[i-1:i+1]) == False:
            return False
    return True

def collinear(list_of_tuples):
    assert same_length(list_of_tuples)
    if len(list_of_tuples) <= 2:
        return True
    else:
        length = len(list_of_tuples[0])
        deltas = []
        for i in range(1, len(list_of_tuples)):
            delta = []
            for j in range(length):
                delta.append(list_of_tuples[i][j]-list_of_tuples[i-1][j])
            deltas.append(tuple(delta))
    return proportional_list(deltas)

    
