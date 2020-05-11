import numpy as np

x1 = np.arange(18,27).reshape(3,3)
x2 = np.arange(52,20,-2).reshape(4,4)
print(x1)
print("")
print(x2)
print("")
print(x1.min(axis=1))
print(x2.min(axis=1))
print(x1.min(axis=0))
print(x2.min(axis=0))