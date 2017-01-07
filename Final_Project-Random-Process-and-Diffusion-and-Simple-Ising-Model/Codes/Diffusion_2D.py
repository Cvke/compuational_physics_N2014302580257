# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:02:50 2017

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def density(t_end):

    x = np.linspace(-20,20,41)
    y = np.linspace(-20,20,41)
    x,y = np.meshgrid(x,y)
    d = np.zeros((41,41))
    d[20][20]=1
    d1 = deepcopy(d)

    for t in range(t_end):
        for i in range(41):
            for j in range(41):
                if i==0 or i==40 or j==0 or j==40:
                    pass
                else:
                    d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])
        d1=deepcopy(d)

    for i in range(41):
            for j in range(41):
                if i==0 or i==40 or j==0 or j==40:
                    pass
                else:
                    if d[i][j]==0:
                        d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])

    return x,y,d
t=int(input('please input the time:'))
x,y,z = density(t)[0],density(t)[1],density(t)[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,rstride=1, cstride=1,cmap = cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlim(0, 0.06)
ax.set_title('Density distribution in 2 dimension, t=%d'%t)
plt.xlim(-20,20)
plt.ylim(-20,20)



plt.show()