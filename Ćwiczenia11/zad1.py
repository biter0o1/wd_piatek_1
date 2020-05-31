import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca( projection = '3d' )

z = np.linspace(0,2 * np.pi,100)
x=np.sin(z)
y=2*np.cos(z)

ax.plot(x,y,z)

plt.show()