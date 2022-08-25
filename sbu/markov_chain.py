import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# Function to generate a random initial probability distribution vector
def initial_vector(n):
    # Create random n-vector
    vec = np.random.random(n)
    
    # Scale the entries
    vec /= vec.sum()

    return vec

# Function to create a random transition matrix
def transition_matrix(n):
    # Create a random n-by-n matrix
    matrix = np.random.rand(n,n)
    
    # Scale the entries for each row
    for row in range(n):
        matrix[row] /= matrix[row].sum()

    return matrix

# Function to compute the transition for N steps
def transition_compute(inital, trans_matrix, n, N):
    # Assign the initial value
    p_transition = inital
    
    # For loop to compute the transition after N steps
    for _ in range(N):
        p_transition = np.matmul(trans_matrix.T,p_transition)
    
    return p_transition

# Function to compute the eigenvector of P.T corresponding to the largest eigenvalue
def stationary(trans_matrix):
    
    # Compute all eigenvectors and their corresponding eigenvalues 
    e_vals, e_vecs = np.linalg.eig(trans_matrix.T)
    
    # Find eigenvector corresponding to the largest eigenvalue     
    p_stationary = e_vecs[np.argmax(e_vals)]
    # Scale the eigenvector
    p_stationary /= p_stationary.sum()
    # Return the real part of the eigenvector
    p_stationary = p_stationary.real
    
    return p_stationary

# Function to plot the norm (p - p_stationary) for N steps
def norm_plot(inital, p_stationary, trans_matrix, N):
    # Assign the initial value for transition vector
    p_trans = inital
    
    # Generate empty array for each steps and their corresponding norm
    step = []
    norm = []    
    
    for i in range(N):
        # Compute the transition vector after i+1 steps
        p_trans = np.matmul(trans_matrix.T, p_trans)
        # Store the norm value
        norm.append(np.linalg.norm(p_trans - p_stationary))
        # Store step-th
        step.append(i + 1)
        # Print step-th and its correspoding norm to console
        print(i+1, np.linalg.norm(p_trans - p_stationary))
    
    # Plot norm agains steps
    plt.plot(step, norm ,".-")
    plt.xlabel("Steps")
    plt.ylabel("|| p - p$_{stationary}$ ||")
    plt.show()

# Main function
def main():
    n = int(input("Enter n: "))
    N = int(input("Enter N-steps: "))
    
    initial_vec = initial_vector(n)
    print("1. A random {}-vector (a probability distribution p):\n{}\n".format(n,initial_vec))
    
    trans_matrix = transition_matrix(n)
    print("2. A random {}-by-{} matrix (a transition matrix P):\n{}\n".format(n,n,trans_matrix))
    
    transition = transition_compute(initial_vec, trans_matrix, n, N)
    print("3. A transition vector for {} steps:\n{}\n".format(N, transition))
    
    eigen_vector = stationary(trans_matrix)
    print("4. The eigenvector of the transpose of matrix P corresponding to the largest eigenvalue:\n{}\n".format(eigen_vector))
    
    print("5. The plot of norm(p - p_stationary) against steps./nThe step-th and its correspoding norm are printed in the console: ")
    norm_plot(initial_vec, eigen_vector, trans_matrix, N)
    
    
if __name__ == "__main__":
    main()
