# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:38:58 2017

@author: Administrator
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave = np.zeros(101)
x_y0 = np.zeros(101)
x_now = np.zeros(5000)

for i in range(100):
    for j in range(5000):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
    average = sum(x_now)/5000
    x_ave[i+1] = average
    
plt.scatter(steps, x_ave, color='m', s= 4,label='Simulation Point')
plt.plot(steps, x_y0, label='Expected Value')
plt.legend(loc='upper right')
plt.text(10,0.65,'5000 walkers',fontsize=12)
plt.text(10,0.5,'step length = 1',fontsize=12)
plt.xlim(0,100)
plt.ylim(-1,1)
plt.grid(True)
plt.xlabel('step number n')
plt.ylabel('$<x>$')
plt.title('$<x>-n$')

plt.show()

