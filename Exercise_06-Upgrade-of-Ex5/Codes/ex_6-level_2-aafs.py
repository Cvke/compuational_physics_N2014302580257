# -*- coding: utf-8 -*-
"""
@author: Chenducvke
"""

import math
import matplotlib.pyplot as plt
#calculate the trajectory
class Cannon:
   def __init__(self,iv=0,la=0,ts=0.01,hwv=0,ax=0,ay=0):
      self.v_i=iv
      self.theta=la
      self.dt=ts
      self.v_hw=hwv
      self.x_aim=ax
      self.y_aim=ay
   def Trajectory(self):
# determine the varibles and parameters
      vx=[self.v_i * math.cos(self.theta * math.pi/180)]
      vy=[self.v_i * math.sin(self.theta * math.pi/180)]
      x=[0.0]
      y=[0.0]
      v=[self.v_i]
      a=6.5*10**(-3)
      alpha=2.5
      B=4*10**(-5)
      T0=300.0
      g=9.8
      def rho(height):
         return (1-a*height/T0)**alpha
# Euler Method
      while (y[-1]>=0)&(vx[-1]>=0):
         ax3, ay3=-B*rho(y[-1])*(v[-1]-self.v_hw)*(vx[-1]-self.v_hw),-g-B*rho(y[-1])*(v[-1]-self.v_hw)*vy[-1]
         x_new = x[-1] + vx[-1]*self.dt
         y_new = y[-1] + vy[-1]*self.dt
         vx_new = vx[-1] + ax3*self.dt
         vy_new = vy[-1] + ay3*self.dt
         v_new = math.sqrt(vx_new**2 + vy_new**2) 
         x.append(x_new)
         y.append(y_new)
         vx.append(vx_new)
         vy.append(vy_new)
         v.append(v_new)
# determine the land point and the maximum height
      r = -float(y[-2]/y[-1])
      xl = (x[-2]+r*x[-1])/(r+1)
      yl = 0
      x[-1] = xl
      y[-1] = yl
      ym=max(y)
      s=[x,y,xl,yl,ym,self.v_i,self.theta,self.dt,self.v_hw]
      return s			
   def Precise_strike(self):
      x_aim=float(input('xaim'))
      y_aim=float(input('yaim'))
      v_hw=float(input('Set headwind speed (m/s):'))
      if (v_hw<=0 or v_hw>=15):
         print('Please input legal parameters:headwind speed should be in range (0,15)(m/s)')
      self.Precise_strike(self)
      k=0
      T=[]
      dt=float(input('Set time step (s):'))
      for cyc1 in range(70000):
         for cyc2 in range(7000):
            A=self.Trajectory(v_hw+cyc1*0.1,20+cyc2*0.01,dt,v_hw,dt,y_aim)
            if ((A[2]-x_aim)^2+(A[3]-y_aim)^2 < 0.01):
                 k=k+1
                 T.append(A)
      for l in range(1,k,1):											
         if (l==1):
           RT_mostaccurate=T[l]
         else:
           if ((RT_mostaccurate[2]-x_aim)^2+(RT_mostaccurate[3]-y_aim)^2>(T[l][2]-x_aim)^2+(T[l][3]-y_aim)^2):
              RT_mostaccurate=T[l]
      for n in range(1,k,1):											
         if (n==1):
           RT_mostefficient=T[n]
         else:
           if (RT_mostefficient[5]>T[n][5]):
              RT_mostefficient=T[n]
      RT=[RT_mostaccurate,RT_mostefficient]
      return RT
def main():
   a=Cannon.Precise_strike
   plt.plot(a[0][0],a[0][1],'m',linestyle='-',linewidth=1.5,label='Accurate')
#generalize the details of the plot    
   plt.grid(True,color='k')
   plt.title('Trajectory of Cannon Shell with Auxiliary Accurate Firing System')
   plt.xlabel('Horizon Distance $x(m)$')
   plt.ylabel('Vertical Distance $y(m)$')
   plt.text(1.05*a[0][3],1.2*a[0][4],'Initial Speed=%.2fm/s'%a[0][5],color='b')
   plt.text(1.05*a[0][3],1.05*a[0][4],'Launch Angle=%.2f°'%a[0][6],color='b')
   plt.text(1.05*a[0][3],0.9*a[0][4],'Time Step=%1.2f$s$'%a[0][7],color='b')
   plt.text(1.05*a[0][3],0.75*a[0][4],'Headwind Speed=%.2fm/s'%a[0][8],color='b')
   plt.text(1.05*a[0][3],0.6*a[0][4],'Land Point=%.2fm'%a[0][2],color='g')
   plt.text(1.05*a[0][3],0.45*a[0][4],'Max Height=%.2fm'%a[0][3],color='g')
   plt.plot(a[1][0],a[1][1],'m',linestyle='-',linewidth=1.5,label='Efficient')
   plt.text(1.05*a[1][3],1.2*a[1][4],'Initial Speed=%.2fm/s'%a[1][5],color='b')
   plt.text(1.05*a[1][3],1.05*a[1][4],'Launch Angle=%.2f°'%a[1][6],color='b')
   plt.text(1.05*a[1][3],0.9*a[1][4],'Time Step=%1.2f$s$'%a[1][7],color='b')
   plt.text(1.05*a[1][3],0.75*a[1][4],'Headwind Speed=%.2fm/s'%a[1][8],color='b')
   plt.text(1.05*a[1][3],0.6*a[1][4],'Land Point=%.2fm'%a[1][2],color='g')
   plt.text(1.05*a[1][3],0.45*a[1][4],'Max Height=%.2fm'%a[1][3],color='g')
   plt.xlim(0,1.8*a[0][3])
   plt.ylim(0,1.5*a[0][4])
   plt.xlim(0,1.8*a[0][3])
   plt.ylim(0,1.5*a[0][4])
   plt.legend()
   plt.show()
main()

      
	
	
	
	
	
	
	
	
	
	
	
