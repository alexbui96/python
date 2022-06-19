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

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.animation as animation

N_max = 1000

prime_list = sieve(N_max)

fig = plt.figure()
ax = fig.add_subplot()

def animate():
    xs = []
    ys = []
    for i in range (4, N_max + 1, 2):
        temp = 0
        j = 0
        while prime_list[j] <= i/2:
            if (i - prime_list[j]) in prime_list:
                temp += 1
            j += 1
        xs.append(i)
        ys.append(temp)
    
        ax.clear()
        ax.plot(xs,ys,'.')

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
