# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 17:04:28 2017

@author: Administrator
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x2_ave = np.zeros(101)
x_y0 = np.zeros(101)
x_now = np.zeros(5000)
x2_now = np.zeros(5000)

for i in range(100):
    for j in range(5000):
        length = 2*np.random.rand() - 1
        x_now[j] = x_now[j] + length
        x2_now[j] = x_now[j]**2
    average2 = sum(x2_now)/5000
    x2_ave[i+1] = average2
    
para = np.polyfit(steps, x2_ave,1)
poly = np.poly1d(para)
y_fit = poly(steps)

plt.scatter(steps, x2_ave,color='r',s=3,label = 'Simulation Point')
plt.plot(steps, y_fit, 'b', label = 'Expected Value')
plt.legend(loc='upper left')
plt.text(7,34,'5000 walkers',fontsize=12)
plt.text(7,30,'random step length',fontsize=12)
plt.xlim(0,100)
plt.ylim(0,50)
plt.grid(True)
plt.xlabel('step number n')
plt.ylabel('$<x^2>$')
plt.title('$<x^2>-n$')

plt.show()