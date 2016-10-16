# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 02:56:55 2016

@author: Administrator
"""

"""
@author: Chenducvke
"""

import math
import matplotlib.pyplot as plt
#calculate the trajectory
def Trajectory(iv,theta,dt):
    vx=[iv * math.cos(theta * math.pi/180)]
    vy=[iv * math.sin(theta * math.pi/180)]
    x=[0.0]
    y=[0.0]
    v=[iv]
    a=6.5*10**(-3)
    alpha=2.5
    B=4*10**(-5)
    T0=300.0
    def rho(height):
            return (1-a*height/T0)**alpha
    
    while (y[-1]>=0)&(vx[-1]>=0):
        ax3, ay3=-B*rho(y[-1])*v[-1]*vx[-1],-9.8-B*rho(y[-1])*v[-1]*vy[-1]
        x_new = x[-1] + vx[-1]*dt
        y_new = y[-1] + vy[-1]*dt
        vx_new = vx[-1] + ax3*dt
        vy_new = vy[-1] + ay3*dt
        v_new = math.sqrt(vx_new**2 + vy_new**2) 
        x.append(x_new)
        y.append(y_new)
        vx.append(vx_new)
        vy.append(vy_new)
        v.append(v_new)
    # determine the land point and the maximum height
    r = -float(y[-2]/y[-1])
    xl = (x[-2]+r*x[-1])/(r+1)
    yl=0
    x[-1] = xl
    y[-1] = yl
    ym=max(y)
    s=[x,y,dt,xl,ym]
    return s
				
				
#plot the figure for various angles
def main():
   theta=float(input('set angle(°)'))
   dt=float(input('set dt(s)'))
   for i in range(7):
    iv=i*20+500
    d=Trajectory(iv,theta,dt)
    plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label='%.2fm/s'%iv)
#generalize the details of the plot    
   plt.grid(True,color='k')
   plt.title('Trajectory of Cannon Shell with Air Drag and Density Correction')
   plt.xlabel('Horizon Distance $x(m)$')
   plt.ylabel('Vertical Distance $y(m)$')
   plt.text(0.1*d[3],1.3*d[4],'Launch Angle=%.2f°'%theta,color='b')
   plt.text(0.1*d[3],1.2*d[4],'Time Step=%1.2fs'%d[2],color='b')
   plt.xlim(0,1.5*d[3])
   plt.ylim(0,1.5*d[4])
   plt.legend()
   plt.show()
   plt.savefig('chapter2.png',dpi = 144)
main()