# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 02:05:04 2016

@author: Administrator
"""
import matplotlib.pyplot as plt
import numpy as np
class billiard_ellipse:   ### x^2/3+y^2/2 = 1
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
            if (self.x[i]**2/3+self.y[i]**2/2 > 1.0):
                self.x[i],self.y[i] = self.correct('x**2/3+y**2/2 < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect((2./3)*self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y       
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt        
    def reflect(self,x,y,vx,vy):
        module = np.sqrt(x**2+y**2)  ### normalization
        x = x/module
        y = y/module
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*y)/v
        cos2 = (vx*y-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*y
        vy_n = vt*y-vc*x
        return vx_n,vy_n
        								
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta < 2*np.pi:
            x.append(np.sqrt(3)*np.cos(theta))
            y.append(np.sqrt(2)*np.sin(theta))
            theta+= 0.01
        plt.plot(x,y,'m')


    def plot(self):
        plt.figure(figsize = (8,8))
        plt.xlabel('$x(\mathrm {m})$',fontsize=12)
        plt.ylabel('$y(\mathrm {m})$',fontsize=12)
        plt.title('Billiard Trajectory in Ellipse($x^2/3+y^2/2 = 1$) Stadium',fontsize=16)
        plt.text(2.05,0.75,'$v_{x0}=%.2f\mathrm {m/s}$'%self.vx_0,fontsize=12)	
        plt.text(2.05,0.6,'$v_{y0}=%.2f\mathrm {m/s}$'%self.vy_0,fontsize=12)	
        plt.text(2.05,0.45,'$x_{0}=%.2f\mathrm {m}$'%self.x_0,fontsize=12)
        plt.text(2.05,0.3,'$y_{0}=%.2f\mathrm {m}$'%self.y_0,fontsize=12)	
        self.plot_boundary()
        plt.plot(self.x,self.y,'g')
        plt.show()
        
    def phase_space_plot(self):
        plt.figure(figsize = (8,8))
							
        plt.title('Phase Space Diagram($x-v_x$)in Ellipse($x^2/3+y^2/2 = 1$) Stadium',fontsize=16)								
        plt.xlabel('$x(\mathrm {m})$',fontsize=12)
        plt.ylabel('$v_x(\mathrm {m/s})$',fontsize=12)
        plt.text(1.55,0.3,'$v_{x0}=%.2f\mathrm {m/s}$'%self.vx_0,fontsize=12)	
        plt.text(1.55,0.25,'$v_{y0}=%.2f\mathrm {m/s}$'%self.vy_0,fontsize=12)	
        plt.text(1.55,0.2,'$x_{0}=%.2f\mathrm {m}$'%self.x_0,fontsize=12)
        plt.text(1.55,0.15,'$y_{0}=%.2f\mathrm {m}$'%self.y_0,fontsize=12)									
        plt.scatter(self.x,self.vx, color='r',s=1)
        plt.show()
    
    def phase_plot(self):
        plt.figure(figsize = (8,8))							
        plt.title('Phase Space Section($x-v_x$) in Ellipse($x^2/3+y^2/2 = 1$) Stadium',fontsize=16)		
        plt.xlabel('$x(\mathrm {m})$',fontsize=12)
        plt.ylabel('$v_x(\mathrm {m/s})$',fontsize=12)								
        record_x = []
        record_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                record_vx.append(self.vx[i])
                record_x.append(self.x[i])
        plt.xlabel('$x(\mathrm {m})$',fontsize=12)
        plt.ylabel('$v_x(\mathrm {m/s})$',fontsize=12)
        plt.text(0.85,0.3,'$v_{x0}=%.2f\mathrm {m/s}$'%self.vx_0,fontsize=12)	
        plt.text(0.85,0.25,'$v_{y0}=%.2f\mathrm {m/s}$'%self.vy_0,fontsize=12)	
        plt.text(0.85,0.2,'$x_{0}=%.2f\mathrm {m}$'%self.x_0,fontsize=12)
        plt.text(0.85,0.15,'$y_{0}=%.2f\mathrm {m}$'%self.y_0,fontsize=12)									
        plt.scatter(record_x,record_vx,color='r',s=2)
        plt.show()
                

A = billiard_ellipse(0.5,0.5,0.3,0.323,62000,0.1)
A.motion_calculate()
A.plot()
A.phase_space_plot()
A.phase_plot()


