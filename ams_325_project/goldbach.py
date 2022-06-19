def sieve(n):
    
    # Create a n-element True array
    prime_list_temp = [True for i in range(n+1)]
    
    # Create a empty prime list
    prime_list = []
    
    # Assign False value for 0 and 1
    prime_list_temp[0] = False
    prime_list_temp[1] = False
    
    # Find sqrt of n
    for i in range(n):
        res = i*i
        if res > n:
            break
    
    for j in range(2, i):
        if prime_list_temp[j]:
            for m in range(j*j, n+1, j):
                prime_list_temp[m] = False
    
    # Store prime number    
    for k in range(n+1):
        if prime_list_temp[k]:
            prime_list.append(k)
            
    return prime_list

    def goldbach(n):
    list = sieve(n)
    goldbach = []
    for i in range(4, n+1, 2):
        j = 0
        while list[j] <= i/2:
            if (i - list[j]) in list:
                goldbach.append((i, list[j], i-list[j]))
            
            j = j + 1
                    
    return goldbach

def goldbach_partition(n):
    list = goldbach(n)
    goldbach_partition_list =[]
    for i in range(4, n+1, 2):
        temp = 0
        
        for j in range(len(list)):
            if list[j][0] == i:
                temp = temp + 1
        goldbach_partition_list.append((i, temp))
    
    return goldbach_partition_list



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from drawnow import drawnow

N_max = 10000

prime_list = sieve(N_max)

mod_0 = []
mod_0_p = []
mod_2 = []
mod_2_p = []
mod_4 = []
mod_4_p = []

plt.ion()

def makeFig():
    plt.plot(mod_0, mod_0_p, 'r.')
    plt.plot(mod_2, mod_2_p, 'y.')
    plt.plot(mod_4, mod_4_p, 'b.')


for i in range (4, N_max + 1, 2):
    temp = 0
    j = 0
    while prime_list[j] <= i/2:
        if (i - prime_list[j]) in prime_list:
            temp += 1
        j += 1
    print(i,temp)
    
    if i%6 == 0:
        mod_0.append(i)
        mod_0_p.append(temp)
    elif i%6 == 2:
        mod_2.append(i)
        mod_2_p.append(temp)
    else:
        mod_4.append(i)
        mod_4_p.append(temp)
    
    drawnow(makeFig)
    plt.pause(.0001)

    plt.savefig('data.png')