import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) / (3 * x)

x = np.linspace(0, 10, 400)  
y = f(x)

plt.plot(x, y)
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="r")
plt.grid(True)
plt.show()