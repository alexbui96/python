import numpy as np

def random_vector(n):
    vec = np.random.random(n)
    vec /= vec.sum()

    return vec

def transition_maxtrix(n)

    matrix = np.random.rand(n,n)
    for row in range(n):
        matrix[row] /= matrix[row].sum()

    return matrix

def transition_compute(N):


