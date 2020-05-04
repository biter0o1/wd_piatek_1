import numpy as np

def funkcja(m,n):
    x = np.logspace(1,n,num=n,base=2)
    return x
print(funkcja(2,4))