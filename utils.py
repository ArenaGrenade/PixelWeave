import numpy as np
from random import random

def random_in_unit_sphere():
    p = np.ones(3)
    while np.dot(p, p) >= 1:
        p = 2 * np.array([random(), random(), random()]) - np.ones(3)
    return p

def random_in_unit_disk():
    p = np.array([1, 1, 0])
    while np.dot(p, p) >= 1:
        p = 2 * np.array([random(), random(), 0]) - np.array([1, 1, 0])
    return p

def unit_vector(array):
    return array / np.linalg.norm(array)
