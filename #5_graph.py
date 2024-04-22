import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**2 + x + 10/(2*x)) / (2*x)

x = np.linspace(0.1, 5, 400)  
y = f(x)

plt.plot(x, y)
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="r")
plt.grid(True)
plt.show()
