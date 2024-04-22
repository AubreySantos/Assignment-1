import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 + x**3 + x**2 + x + 1

x = np.linspace(-2, 2, 400)
y = f(x)

plt.plot(x, y)
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="r")
plt.grid(True)
plt.show()
