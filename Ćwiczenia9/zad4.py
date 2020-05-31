import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv('Ćwiczenia9/iris.data')
x = iris['petal length']
y = iris['petal width']
plt.scatter(x,y, c=np.random.randint(0,150,150))
plt.show()

