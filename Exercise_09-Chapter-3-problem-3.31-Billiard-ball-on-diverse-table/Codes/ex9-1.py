# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 02:05:04 2016

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np

class billiard_rectangular:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
    
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i] < -1.0):
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.x[i] > 1.0):
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.y[i] < -1.0):
                self.x[i],self.y[i] = self.correct('y>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i]
            elif(self.y[i] > 1.0):
                self.x[i],self.y[i] = self.correct('y<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i] 
            else:
                pass
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y
    
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
    
    def reflect(self):
        pass
    
    def plot(self):
        plt.figure(figsize = (8,8))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('$x(\mathrm {m})$',fontsize=12)
        plt.ylabel('$y(\mathrm {m})$',fontsize=12)
        plt.title('Billiard Trajectory in Rectangular Stadium',fontsize=16)
        plt.text(1.05,0.75,'$v_{x0}=%.2f\mathrm {m/s}$'%self.vx_0,fontsize=12)	
        plt.text(1.05,0.6,'$v_{y0}=%.2f\mathrm {m/s}$'%self.vy_0,fontsize=12)	
        plt.text(1.05,0.45,'$x_{0}=%.2f\mathrm {m}$'%self.x_0,fontsize=12)
        plt.text(1.05,0.3,'$y_{0}=%.2f\mathrm {m}$'%self.y_0,fontsize=12)								
        plt.plot(self.x,self.y,color='m')
        plt.show()
								
A = billiard_rectangular(0.3,0.7,0.62,0.33,3000,0.1)
A.motion_calculate()
A.plot()
