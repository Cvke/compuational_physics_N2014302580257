# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 02:51:48 2016

@author: Administrator
"""

import math as mt
import matplotlib.pyplot as plt

# define a function that given amplitude of force, gives theta,omega and t

def change_amp(F,T):   
    # define some constants
    l = 9.8
    g = 9.8
    q=0.3
    f = float(2/3)
    dt = 0.08
    theta0 = 0.2
    omega0 = 0
    theta = [theta0]
    omega = [omega0]
    t = [0]
    # move the pendulum
    while t[-1] < T:
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
    return theta,omega,t

def main():
	F = float(input('Please set the driven force amplitude:'))
	T = float(input('Please set the running time:'))
	theta_0 = change_amp(F,T)[0]
	omega_0 = change_amp(F,T)[1]
	plt.scatter(theta_0,omega_0,s=8,color='r',label='$F_D=%.2f'%F)
	plt.text(0.7*max(theta_0),0.8*max(omega_0),'$F_D=$%.2f'%F,fontsize=14)
	plt.title('$\\omega$-$\\theta$',fontsize=17)
	plt.xlabel('$\\theta(\mathrm {rads/s})$',fontsize=15)
	plt.ylabel('$\\omega(\mathrm {rads})$',fontsize=15)
	plt.grid(True)	
	plt.show()
	
main()