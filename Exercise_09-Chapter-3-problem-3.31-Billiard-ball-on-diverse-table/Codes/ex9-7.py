# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:16:23 2016

@author: Administrator
"""
from numpy import * 
import matplotlib.pyplot as plt

# class: BILLIARD solves for a stadium-shaped boundary
# where:
#        x0, y0, vx0, vy0: initial position of billiard 
#        dt, time : time step and total time
#        alpha: the length cube region 
class BILLIARD(object):
    def __init__(self,_alpha=0.,_r=1.,_x0=0.2,_y0=0.,_vx0=0.6,_vy0=0.8,_dt=0.001,_time=100):
        self.alpha, self.r, self.dt, self.time, self.n = _alpha, _r, _dt, _time, int(_time/_dt)
        self.x, self.y, self.vx, self.vy = [_x0], [_y0], [_vx0], [_vy0]
    def cal(self):            # use Euler method to solve billiard motion
        for i in range(self.n):
            self.nextx = self.x[-1]+self.vx[-1]*self.dt
            self.nexty = self.y[-1]+self.vy[-1]*self.dt
            self.nextvx, self.nextvy = self.vx[-1], self.vy[-1]
            if (self.nexty>self.alpha*self.r and self.nextx**2+(self.nexty-self.alpha*self.r)**2>self.r**2) \
                    or (self.nexty<-self.alpha*self.r and self.nextx**2+(self.nexty+self.alpha*self.r)**2>self.r**2) \
                    or (self.nextx>self.r) \
                    or (self.nextx<-self.r):
                self.nextx=self.x[-1]
                self.nexty=self.y[-1]
                while not( \
                        (self.nexty>self.alpha*self.r and self.nextx**2+(self.nexty-self.alpha*self.r)**2>self.r**2) \
                        or (self.nexty<-self.alpha*self.r and self.nextx**2+(self.nexty+self.alpha*self.r)**2>self.r**2) \
                        or (self.nextx>self.r) \
                        or (self.nextx<-self.r)):
                    self.nextx=self.nextx+self.nextvx*self.dt/100
                    self.nexty=self.nexty+self.nextvy*self.dt/100
                if self.nexty>self.alpha*self.r:
                    self.v = array([self.nextvx,self.nextvy])
                    self.norm =  1/self.r*array([self.nextx, self.nexty-self.alpha*self.r])
                    self.v_perpendicular = dot(self.v, self.norm)*self.norm
                    self.v_parrallel = self.v-self.v_perpendicular
                    self.v_perpendicular= -self.v_perpendicular
                    self.nextvx, self.nextvy= (self.v_parrallel+self.v_perpendicular)[0],(self.v_parrallel+self.v_perpendicular)[1]
                elif self.nexty<-self.alpha*self.r:
                    self.v = array([self.nextvx,self.nextvy])
                    self.norm =  1/self.r*array([self.nextx, self.nexty+self.alpha*self.r])
                    self.v_perpendicular = dot(self.v, self.norm)*self.norm
                    self.v_parrallel = self.v-self.v_perpendicular
                    self.v_perpendicular= -self.v_perpendicular
                    self.nextvx, self.nextvy= (self.v_parrallel+self.v_perpendicular)[0],(self.v_parrallel+self.v_perpendicular)[1]
                else:
                    self.nextvx, self.nextvy= -self.nextvx, self.nextvy
            self.x.append(self.nextx)
            self.y.append(self.nexty)
            self.vx.append(self.nextvx)
            self.vy.append(self.nextvy)
    def plot_position(self,_ax):        # give trajectory plot
        _ax.plot(self.x,self.y,'-b',color='g',label=r'$\alpha=$'+'  %.2f'%self.alpha)
        _ax.plot([self.r]*10,linspace(-self.alpha*self.r,self.alpha*self.r,10),'-k',color='c',lw=2)
        _ax.plot([-self.r]*10,linspace(-self.alpha*self.r,self.alpha*self.r,10),'-k',color='c',lw=2)
        _ax.plot(self.r*cos(linspace(0,pi,100)),self.r*sin(linspace(0,pi,100))+self.alpha*self.r,'-k',color='m',lw=2)
        _ax.plot(self.r*cos(linspace(pi,2*pi,100)),self.r*sin(linspace(pi,2*pi,100))-self.alpha*self.r,'-k',color='m',lw=2)
    def plot_phase(self,_ax,_secy=0):        # give phase-space plot
        self.secy=_secy
        self.phase_x, self.phase_vx = [], []
        for i in range(len(self.x)):
            if abs(self.y[i]-self.secy)<1E-3 :
                self.phase_x.append(self.x[i])
                self.phase_vx.append(self.vx[i])
        _ax.plot(self.phase_x,self.phase_vx,'ob',markersize=2,label=r'$\alpha=$'+'  %.2f'%self.alpha)


# give a trajectory and phase space plot          
fig= plt.figure(figsize=(16,16))
#ax1=plt.axes([0.1,0.55,0.35,0.35])
#ax2=plt.axes([0.6,0.55,0.35,0.35])
#ax3=plt.axes([0.1,0.1,0.35,0.35])
ax4=plt.axes([0.6,0.1,0.35,0.35])
#ax1.set_xlim(-1.1,1.1)
#ax2.set_xlim(-1.1,1.1)
#ax3.set_xlim(-1.1,1.1)
ax4.set_xlim(-1.1,1.1)
#ax1.set_ylim(-1.1,1.1)
#ax2.set_ylim(-1.1,1.1)
#ax3.set_ylim(-1.1,1.1)
ax4.set_ylim(-1.1,1.1)
#ax1.set_xlabel(r'$x (m)$',fontsize=18)
#ax1.set_ylabel(r'$y (m)$',fontsize=18)
#ax1.set_title('Circular stadium: trajectory',fontsize=18)
#ax2.set_xlabel(r'$x (m)$',fontsize=18)
#ax2.set_ylabel(r'$v_x (m/s)$',fontsize=18)
#ax2.set_title('Circular stadium: phase-space',fontsize=18)
#ax3.set_xlabel(r'$x (m)$',fontsize=12)
#ax3.set_ylabel(r'$y (m)$',fontsize=12)
#ax3.set_title('Billiard'+' trajectory'+' when $\\alpha=0.1$',fontsize=16)
ax4.set_xlabel(r'$x (m)$',fontsize=12)
ax4.set_ylabel(r'$v_x (m/s)$',fontsize=12)
ax4.set_title('Phase'+' Section'+' when $\\alpha=0.1$',fontsize=16)


cmp=BILLIARD(0.1)
cmp.cal()
cmp.plot_position(ax3)
cmp.plot_phase(ax4)

plt.show()
