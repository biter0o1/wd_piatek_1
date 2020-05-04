import numpy as np

def funkcja(n):
    x = np.arange(n,0,-1)
    diag = np.diag(x)
    return diag


print(funkcja(3))