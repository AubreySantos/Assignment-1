import matplotlib.pyplot as plt
import math

ans = []
for i in range (-10, 10, 1):
    x = i**10 - i**8 + i**2 - 8
    ans.append(x)
    print(ans)

plt.plot(range(-10,10),ans)
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="r")
plt.grid(True)
plt.show()