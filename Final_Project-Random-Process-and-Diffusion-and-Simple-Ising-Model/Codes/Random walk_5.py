# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 17:11:17 2017

@author: Administrator
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave = np.zeros(101)
x_now = np.zeros(5000)

for i in range(100):
    for j in range(5000):
        ruler = np.random.rand()
        if ruler<=0.75:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
    average = sum(x_now)/5000
    x_ave[i+1] = average
    
para = np.polyfit(steps, x_ave,1)
poly = np.poly1d(para)
y_fit = poly(steps)

plt.scatter(steps, x_ave,color='m',s=3,label = 'Simulation Point')
plt.plot(steps, y_fit, 'b', label = 'Expected Value')
plt.legend(loc='upper left')
plt.text(7,67,'5000 walkers',fontsize=12)
plt.text(7,60,'step length = 1',fontsize=12)
plt.text(7,53,'P(left) = 0.25, P(right) = 0.75',fontsize=12)
plt.xlim(0,100)
plt.ylim(0,100)
plt.grid(True)
plt.xlabel('step number(= time)')
plt.ylabel('$<x>$')
plt.title('$<x>-n$')

plt.show()