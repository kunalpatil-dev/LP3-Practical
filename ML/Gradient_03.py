import matplotlib.pyplot as plt
import numpy as np

# Function
def f(x):
    return (x + 3)**2

# Derivative
def df(x):
    return 2*(x + 3)

# Gradient Descent
def gradient_descent(start, learning_rate, iterations):
    x = start
    points = [x]

    for _ in range(iterations):
        x = x - learning_rate * df(x)
        points.append(x)

    print("Local minimum occurs at:", x)

    # Plot
    x_vals = np.linspace(-7, 5, 100)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, 'g')                   # curve
    plt.plot(points, f(np.array(points)), '-o')     # descent steps
    plt.title("Gradient Descent on y = (x+3)^2")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()

# Run
gradient_descent(start=2.0, learning_rate=0.2, iterations=50)
