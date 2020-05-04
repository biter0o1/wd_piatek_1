import numpy as np

def funkcja(n):
    x = np.arange(1,n*n+1).reshape((n,n))
    return x

x = funkcja(5)
print(x)