import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,30,0.1)
ysin = np.sin(x)
plt.plot(x,ysin+2,label='sin(x)')
plt.plot(x,-ysin,label='sin(x)')

plt.ylabel("sin(x)")
plt.xlabel("x")

plt.title("Wykres sin(x),sin(x)")
plt.legend(loc='center left')

plt.show()