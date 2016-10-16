# -*- coding: utf-8 -*-
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
    ax1, ay1=0,-9.8
    while y[-1]>=0:
        x_new = x[-1] + vx[-1]*dt
        y_new = y[-1] + vy[-1]*dt
        vx_new = vx[-1] + ax1*dt
        vy_new = vy[-1] + ay1*dt
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
   iv=float(input('set v(m/s)'))
   theta=float(input('set angle(°)'))
   dt=float(input('set dt(s)'))
   d=Trajectory(iv,theta,dt)
   plt.plot(d[0],d[1],'m',linestyle='-',linewidth=1.5,label='trajectory')
#generalize the details of the plot    
   plt.grid(True,color='k')
   plt.title('Trajectory of Cannon Shell with No Air Drag')
   plt.xlabel('Horizon Distance $x(m)$')
   plt.ylabel('Vertical Distance $y(m)$')
   plt.text(1.1*d[3],1.2*d[4],'Initial Speed=%.2fm/s'%iv,color='b')
   plt.text(1.1*d[3],1.05*d[4],'Launch Angle=%.2f°'%theta,color='b')
   plt.text(1.1*d[3],0.9*d[4],'Time Step=%1.2fs'%d[2],color='b')
   plt.text(1.1*d[3],0.75*d[4],'Land Point=%.2fm'%d[3],color='g')
   plt.text(1.1*d[3],0.6*d[4],'Max Height=%.2fm'%d[4],color='g')
   plt.xlim(0,1.8*d[3])
   plt.ylim(0,1.5*d[4])
   plt.legend()
   plt.show()
   plt.savefig('chapter2.png',dpi = 144)
main()
