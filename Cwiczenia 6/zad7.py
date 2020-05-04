import numpy as np

def funkcja(n):
    x = np.diag([2 for i in range(0,n)])
    for i in range(0,n-1):
        x[i+1,0] = x[i,0]+2
        x[0,i+1] = x[0,i]+2

    for i in range(0,n):
        pomoc = 0
        for j in range(0,n):
            if x[i,j] == 2:
                pomoc = 1
            if x[i,j] < 2 and x[i,j-1] <= 2:
               x[i,j] = x[i,j-1]+2
            elif x[i,j] < 2 and x[i,j-1] > 2 and pomoc == 1:
               x[i,j] = x[i,j-1]+2
            elif x[i,j] < 2 and x[i,j-1] > 2 and pomoc == 0:
               x[i,j] = x[i,j-1]-2
    return x

print(funkcja(10))