# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 03:18:06 2016

@author: Chenducvke
"""

import math as mt
import matplotlib.pyplot as plt

# define a function that given amplitude of force, gives theta,omega and t

def change_amp(pcsn,T,F,f):   
    # define some constants
    l = 9.8
    g = 9.8
    q = 0.5
    dt = mt.pi/50
    theta0 = 0.2
    omega0 = 0
    theta = [theta0]
    omega = [omega0]
    pcsan = [theta0]
    pcsav = [omega0]
    t = [0]
    # move the pendulum
    while t[-1] < T*60*mt.pi:
        omega_new = omega[-1] - ((g/l)*mt.sin(theta[-1]) + q*omega[-1] - F*mt.sin(f*t[-1]))*dt
        omega.append(omega_new)
        theta_new = theta[-1] + omega[-1]*dt
        while theta_new > mt.pi:
            theta_new -= 2*mt.pi
        while theta_new < -mt.pi:
            theta_new += 2*mt.pi
        theta.append(theta_new)
        if (t[-1]-(pcsn*mt.pi)/f)%(3*mt.pi) <= dt:
            pcsan.append(theta_new)
            pcsav.append(omega_new)
        t_new = t[-1] + dt
        t.append(t_new)
    return theta,omega,t,pcsan,pcsav

def main():
	pcsn = float(input('Please set the Poincare sections t in phase with force:'))
	T = float(input('Please set the running time:'))
	F = float(input('Please set the driven force amplitude:'))
	f = float(input('Please set the driven force frequency:'))
	pcsan_0 = change_amp(pcsn,T,F,f)[3]
	pcsav_0 = change_amp(pcsn,T,F,f)[4]
	plt.scatter(pcsan_0,pcsav_0,s=8,color='r')
	plt.text(0.6*max(pcsan_0),0.25,'$F_D=%.2f$'%F,fontsize=14)
	plt.text(0.6*max(pcsan_0),0,'$\\Omega_D=%.5f$'%f,fontsize=14)
	plt.text(0.6*max(pcsan_0),-0.25,'$t=%.2f\\pi$'%pcsn,fontsize=14)
	plt.title('$\\omega$-$\\theta(\mathrm{Poincare\,Sections\,of\,t\,in\,Phase\,with\,F_D})$',fontsize=16)
	plt.xlabel('$\\theta(\mathrm {rads/s})$',fontsize=15)
	plt.ylabel('$\\omega(\mathrm {rads})$',fontsize=15)
	plt.grid(True)	
	plt.show()
	
main()