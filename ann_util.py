import random
import math

def make_matrix(N, M):
    """
    Make an N rows by M columns matrix
    """
    return list([0 for i in range(M)] for i in range(N))

def between(min,max):
    """
    Return a real random value between min and max
    """
    return random.random() * (max - min) + min


def sigmoid(x):
    return 1.0 / (1 + math.exp(-x))
