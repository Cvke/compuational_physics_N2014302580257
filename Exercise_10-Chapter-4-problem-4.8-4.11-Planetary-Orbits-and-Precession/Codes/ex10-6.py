'''
The precession of Mercury
astronomical units
F=GMM'/(r^2)*(1+alpha/(r^2))
'''

import numpy as np
import matplotlib.pyplot as plt
from math import *
import mpl_toolkits.mplot3d

#Determine the initial value
def initial(a,e):
    x0=a*(1+e)
    y0=0
    v_x0=0
    v_y0=2*pi*sqrt((1-e)/(a*(1+e)))
    return [x0,y0,v_x0,v_y0]

def orbits(alpha):
    global a
    a=0.39
    e=0.206
    i_M=initial(a,e)
    x0=i_M[0]
    x=[]
    x.append(x0)
    y0=i_M[1]
    y=[]
    y.append(y0)
    v_x0=i_M[2]
    v_x=[]
    v_x.append(v_x0)
    v_y0=i_M[3]
    v_y=[]
    v_y.append(v_y0)
    r=[]
    r.append(sqrt(x0**2+y0**2))
    t=[]
    t.append(0)
    time=2.0
    dt=0.001

    for i in range(int(time/dt)):
        v_x.append(v_x[i]-4*pi**2*x[i]/(r[i]**3)*(1+alpha/(r[i]**2))*dt)
        x.append(x[i]+v_x[i+1]*dt)
        v_y.append(v_y[i]-4*pi**2*y[i]/(r[i]**3)*(1+alpha/(r[i]**2))*dt)
        y.append(y[i]+v_y[i+1]*dt)
        r.append(sqrt(x[i+1]**2+y[i+1]**2))
        t.append(t[i]+dt)
    return [x,y,v_x,v_y,r,t]

def precession(M):
    x=M[0]
    y=M[1]
    r=M[4]
    t=M[5]
    theta=[]
    xp=[]
    yp=[]
    tp=[]
    for i in range(len(r)-2):
        if (r[i+2]-r[i+1])*(r[i+1]-r[i])<0:#choose the perihelions and aphelions
            if r[i+1]<a:#choose the aphelions
                if x[i+1]>0:
                    angle=arctan(y[i+1]/x[i+1])
                else:
                    angle=pi+arctan(y[i+1]/x[i+1])
                theta.append(angle)
                xp.append(x[i+1])
                yp.append(y[i+1])
                tp.append(t[i+1])
    return [tp,theta,xp,yp]

#The orbits of planet
M1=orbits(0.002)
x_M1=M1[0]
y_M1=M1[1]
p1=precession(M1)
tp1=p1[0]
theta1=p1[1]
xp1=p1[2]
yp1=p1[3]

#plot
fig=plt.figure(figsize=[8,8])
plt.plot(x_M1,y_M1,color='c')
plt.scatter(0,0,s=10,color='orange')
plt.scatter(xp1,yp1,color='green')
plt.title("Mercury's Orbit when "+"$\\alpha=0.002$",fontsize=16)
plt.xlabel('x/AU')
plt.xlim(-0.6,0.6)
plt.ylabel('y/AU')
plt.ylim(-0.6,0.6)

plt.show()