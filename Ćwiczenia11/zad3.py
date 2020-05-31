import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure(figsize=(16,9))
# generuj dane.
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)

colors = ['plasma', 'hsv','tab20','ocean','brg']
# rysuj powierzchnię.
for i in range(1,6):
    ax = fig.add_subplot(2,3,i, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap =plt.get_cmap(colors[i-1]),
    linewidth = 0 , antialiased = True )
    ax.set_zlim(- 1.01 , 1.01 )
    ax.zaxis.set_major_locator(LinearLocator( 10 ))
    ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))


# Dodanie paska kolorów.
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
plt.show()