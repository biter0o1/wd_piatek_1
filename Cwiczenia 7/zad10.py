import numpy as np

x1 = np.arange(81)
print(x1)
x2 = x1.reshape(9,9)
print("\n",x2)
x3 = x2.T
print("\n",x3)
x4 = x3.ravel()
print("\n",x4)
x5 = x4.reshape(27,3)
print(x5)