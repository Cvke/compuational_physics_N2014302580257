# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 03:19:20 2016

@author: Administrator
"""

import math as mt
import matplotlib.pyplot as plt

# define a function that given amplitude of force, gives theta,omega and t

def change_amp(pcsn,T):   
    # define some constants
    l = 9.8
    g = 9.8
    q=0.3
    F=1.2
    f = float(2/3)
    dt = mt.pi/100
    theta0 = 0.2
    omega0 = 0
    theta = [theta0]
    omega = [omega0]
    pcsan = [theta0]
    pcsav = [omega0]
    t = [0]
    # move the pendulum
    while t[-1] < 3000*mt.pi:
        omega_new = omega[-1] - ((g/l)*mt.sin(theta[-1]) + q*omega[-1] - F*mt.sin(f*t[-1]))*dt
        omega.append(omega_new)
        theta_new = theta[-1] + omega[-1]*dt
        while theta_new > mt.pi:
            theta_new -= 2*mt.pi
        while theta_new < -mt.pi:
            theta_new += 2*mt.pi
        theta.append(theta_new)
        t_new = t[-1] + dt
        t.append(t_new)
        if t[-1]%(pcsn*mt.pi) <= dt:
            pcsan.append(theta_new)
            pcsav.append(omega_new)
    return theta,omega,t,pcsan,pcsav

def main():
	pcsn = float(input('Please set the Poincare sections time :'))
	T = float(input('Please set the running time:'))
	pcsan_0 = change_amp(pcsn,T)[3]
	pcsav_0 = change_amp(pcsn,T)[4]
	plt.scatter(pcsan_0,pcsav_0,s=8,color='r')
	plt.text(0.7*max(pcsan_0),0.8*max(pcsav_0),'$F_D=1.2$',fontsize=14)
	plt.title('$\\omega$-$\\theta$',fontsize=17)
	plt.xlabel('$\\theta(\mathrm {rads/s})$',fontsize=15)
	plt.ylabel('$\\omega(\mathrm {rads})$',fontsize=15)
	plt.grid(True)	
	plt.show()
	
main()