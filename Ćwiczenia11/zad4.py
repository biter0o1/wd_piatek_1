import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

fig = plt.figure( figsize =( 6 , 6 ))
ax1 = fig.gca(projection='3d')

_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True,color =colors[np.random.randint(0,8)] )
ax1.set_title('Wykres zacieniony')

plt.show()