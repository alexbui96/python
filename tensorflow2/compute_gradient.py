from tensorflow import *

def compute_gradient(x0):
    
    # define a variable
    x = Variable(x0)

    with GradientTape() as tape:
        tape.watch(x)

        # define y using multiply operation
        y = multiply(x,x)

    # return the gradient of y with respect to x
    return tape.gradient(y, x).numpy()

def main():
    x0 = float(input("Enter initial value: "))
    print(compute_gradient(x0))

if __name__ == "__main__":
    main()