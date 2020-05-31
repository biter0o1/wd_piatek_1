import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
np.random.seed( 40000 )

color = pd.Series(['r','c','g','b','y'])
markers = pd.Series(['^',"P","X",'o','1'])

for i in np.random.randint(0,5,5):
    x = np.random.randint(0,50,50)
    y = np.random.randint(0,50,50)
    z = np.random.randint(0,50,50)
    ax.scatter(x,y,z, c=color[i], marker=markers[i])



plt.show()