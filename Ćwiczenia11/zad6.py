import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 121 , projection = '3d' )
n = 20
x = randrange(n, 1, 21)
y = randrange(n, 1, 21)
z = randrange(n, 1, 21)
ax.scatter(x, y, z, c='r')


ax = fig.add_subplot( 122, projection = '3d' )
n=5
x=randrange(n,1,5)
y=randrange(n,1,5)
z=randrange(n,1,5)
ax.plot(x,y,z,c='g')
plt.show()