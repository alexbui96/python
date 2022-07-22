# some useful libraries
import matplotlib.pyplot as plt
import numpy as np

# ignore errors
np.warnings.filterwarnings("ignore")

# Function generate mandelbrot set
def mandelbrot(n, N_max, threshold):

    # Create points (x,y) in range [-2, 1]x[-1.5, 1.5]
    x, y = np.linspace(-2, 1, n)[:, np.newaxis], np.linspace(-1.5, 1.5, n)[np.newaxis, :]

    # Generate complex numbers correspoinding to the points
    c = x + 1j*y

    # Compute z-values
    z = 0
    for j in range(N_max):
        z = z ** 2 + c

    # Create a boolean array
    mask = abs(z) < threshold

    return x, y, c, z, mask

# Function to plot and save mandelbrot set
def plot_mandelbrot(mask):

    plt.imshow(mask.T, extent= [-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
    plt.show()

# Main function 
def main():
    n = int(input("Enter n: "))
    N_max = int(input("Enter N_max: "))
    threshold = int(input("Enter threshold: "))
    
    x, y, c, z, mask = mandelbrot(n, N_max, threshold)
    
    print("1. The points (x,y):\n{}\nThe c-value:\n{}\n".format(np.meshgrid(x,y), c))
    print("2. The z-value:\n{}\n".format(z))
    print("3. The boolean array mask:\n{}\n".format(mask))
    print("The mandelbrot plot:\n")
    plot_mandelbrot(mask)
    
if __name__ == "__main__":
    main()
