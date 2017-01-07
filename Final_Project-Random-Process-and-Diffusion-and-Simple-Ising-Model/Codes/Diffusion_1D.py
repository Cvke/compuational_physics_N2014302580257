# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:03:23 2017

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def density(t_end):

    x = list(np.linspace(-50,50,101))
    d = list(np.zeros(50)) + list(np.ones(1)) + list(np.zeros(50))
    d1 = deepcopy(d)

    for i in range(t_end):
        for j in range(101):
            if j==0 or j==100:
                pass
            else:
                d[j] = 0.5* (d1[j+1] + d1[j-1])
        d1 = deepcopy(d)

    for i in range(101):
        if i==0 or i==100:
            pass
        else:
            if d[i]==0:
                d[i] = 0.5*(d1[i+1] + d1[i-1])
    return x, d

x1, d1 = density(0)[0], density(0)[1]
x2, d2 = density(10)[0], density(10)[1]
x3, d3 = density(100)[0], density(100)[1]
x4, d4 = density(200)[0], density(200)[1]
x5, d5 = density(300)[0], density(300)[1]

plt.plot(x1,d1,label='t=0')
plt.plot(x2,d2,label='t=10')
plt.plot(x3,d3,label='t=100')
plt.plot(x4,d4,label='t=200')
plt.plot(x5,d5,label='t=300')

plt.xlabel('x')
plt.ylabel('density')
plt.title('Diffusion in one dimension')
plt.xlim(-50,50)
plt.ylim(0,0.3)
plt.grid()
plt.legend()

plt.show()