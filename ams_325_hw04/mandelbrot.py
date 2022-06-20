import matplotlib.pyplot as plt
import numpy as np
np.warnings.filterwarnings("ignore")

n = 512
N_max = 50
threshold = 50


x, y = np.linspace(-2, 1, n), np.linspace(-1.5, 1.5, n)
[x,y] = np.meshgrid(x, y)
c = x + 1j*y

z = 0

for j in range(N_max):
    z = z ** 2 + c
    mask = abs(z) < threshold


plt.imshow(mask.T, extent= [-2, 1, -1.5, 1.5])
plt.gray()
plt.savefig('mandelbrot.png')