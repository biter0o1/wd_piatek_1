import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,30,0.1)
ysin = np.sin(x)
ycos = np.cos(x)
plt.plot(x,ysin,label='sin(x)')
plt.plot(x,ycos,label='cos(x)')

plt.ylabel("sin / cos")
plt.xlabel("x")

plt.legend(loc='upper right')

plt.show()