import numpy as np
def funkcja():
    x = np.arange(0,25)
    x[0] = 1
    x[1] = 1
    for i in range(2,25):
        x[i] = x[i-1] + x[i-2]
    x = x.reshape((5,5))
    return x


print(funkcja())