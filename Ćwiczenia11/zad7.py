import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.gca(projection='3d')
n = 20
x = randrange(n, 1, 21)
y = randrange(n, 1, 21)
z = randrange(n, 1, 21)
ax.scatter(x, y, z, c='r',lw=8)


n=5
x=randrange(n,1,21)
y=randrange(n,1,21)
z=randrange(n,1,21)
ax.plot(x,y,z,c='g',lw=8)
plt.show()