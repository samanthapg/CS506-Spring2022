import math 
import numpy as np 
import scipy 
from scipy import spatial
from scipy.spatial import distance

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):
    if (len(x)==0 or len(y)==0):
        return "length cannot equal 0"
    intersection = len(list(set(x).intersection(set(y))))
    union = set(x).union(set(y))
    return 1 - float(intersection) / len(union)


def cosine_sim(x, y):
    return 1 - spatial.distance.cosine(x, y)


# Feel free to add more
