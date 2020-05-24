import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def rzucaj(n,list):
    for i in range(n):
        a=np.random.randint(1,6)
        b=np.random.randint(1,6)
        c=a+b
        list.append(c)


list =[]
rzucaj(500,list)
plt.hist(list, bins=50, density=True)
plt.grid(True)
plt.xlabel('Wartości')
plt.ylabel('Szansa')
plt.title('Histogram')
plt.show()