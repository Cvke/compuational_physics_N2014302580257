# -*- coding: utf-8 -*-
"""
@author: Chenducvke
"""

import math
import matplotlib.pyplot as plt
#calculate the trajectory
def Trajectory4(v_i,theta,dt,v_hw):
    vx=[v_i * math.cos(theta * math.pi/180)]
    vy=[v_i * math.sin(theta * math.pi/180)]
    x=[0.0]
    y=[0.0]
    v=[v_i]
    a=6.5*10**(-3)
    alpha=2.5
    B=4*10**(-5)
    T0=300.0
    g=9.8
    def rho(height):
       return (1-a*height/T0)**alpha
    
    while (y[-1]>=0)&(vx[-1]>=0):
        ax3, ay3=-B*rho(y[-1])*(v[-1]-v_hw)*(vx[-1]-v_hw),-g-B*rho(y[-1])*(v[-1]-v_hw)*vy[-1]
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
    
def Trajectory1(iv,theta,dt):
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
				
def Trajectory2(iv,theta,dt):
    B=4*10**(-5)
    vx=[iv * math.cos(theta * math.pi/180)]
    vy=[iv * math.sin(theta * math.pi/180)]
    x=[0.0]
    y=[0.0]
    v=[iv]
    
    while (y[-1]>=0)&(vx[-1]>=0):
        ax2, ay2=-B*v[-1]*vx[-1],-9.8-B*v[-1]*vy[-1]
        x_new = x[-1] + vx[-1]*dt
        y_new = y[-1] + vy[-1]*dt
        vx_new = vx[-1] + ax2*dt
        vy_new = vy[-1] + ay2*dt
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
				
def Trajectory3(iv,theta,dt):
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
#plot the figure for various paras
def main():
   v_i=float(input('Set initial speed (m/s):'))
   if (v_i<5 or v_i>6800):
      print('Please input legal parameters:initial speed should be in range [5,6800](m/s)')
      main()			
   theta=float(input('Set luanch angle (°):'))
   if (theta<=0 or theta>=90):
      print('Please input legal parameters:luanch angle should be in range (0,90)(°)')
      main()			
   v_hw=float(input('Set headwind speed (m/s):'))
   if (v_hw<=0 or v_hw>=15 or v_hw>v_i):
      print('Please input legal parameters:headwind speed should be in range (0,15)(m/s)')
      main()			
   dt=float(input('Set time step (s):'))		
   a=Trajectory1(v_i,theta,dt)
   b=Trajectory2(v_i,theta,dt)
   c=Trajectory3(v_i,theta,dt)
   d=Trajectory4(v_i,theta,dt,v_hw)			
   plt.plot(a[0],a[1],'m',linestyle='-',linewidth=1.5,label='No correction')
   plt.plot(b[0],b[1],'g',linestyle='-',linewidth=1.5,label='+Air drug')
   plt.plot(c[0],c[1],'b',linestyle='-',linewidth=1.5,label='+Air density')
   plt.plot(d[0],d[1],'r',linestyle='-',linewidth=1.5,label='+Headwind drug')
#generalize the details of the plot    
   plt.grid(True,color='k')
   plt.title('Trajectory of Cannon Shell in Different Correction')
   plt.xlabel('Horizon Distance $x(m)$')
   plt.ylabel('Vertical Distance $y(m)$')
   plt.text(0.96*a[3],0.70*a[4],'Initial Speed=%.2fm/s'%v_i,color='b')
   plt.text(0.96*a[3],0.55*a[4],'Launch Angle=%.2f°'%theta,color='b')
   plt.text(0.96*a[3],0.4*a[4],'Time Step=%1.2f$s$'%dt,color='b')
   plt.text(0.96*a[3],0.25*a[4],'Headwind Speed=%.2fm/s'%v_hw,color='b')
   plt.xlim(0,1.6*a[3])
   plt.ylim(0,1.3*a[4])
   plt.legend()
   plt.show()
   plt.savefig('chapter2.png',dpi=75)
main()
