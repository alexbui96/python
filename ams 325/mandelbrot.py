import matplotlib.pyplot as plt
import numpy as np

N_max = 50
threshold = 50

x = np.linspace(-2,1,N_max)
y = np.linspace(-1.5,1.5, N_max)


c = x + 1j*y

z = 0

for j in range(N_max):
    z = z**2 + c
    mandelbrot_set = (abs(z) < threshold)
    
print(mandelbrot_set)