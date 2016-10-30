# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 00:37:57 2016

@author: Administrator
"""

import math as mt
import matplotlib.pyplot as plt

# define a function that given amplitude of force, gives theta,omega and t

def change_amp(F,q,T):   
    # define some constants
    l = 9.8
    g = 9.8
    f = float(2/3)
    dt = 0.04
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
	q = float(input('Please set the damping parameter:'))
	T = float(input('Please set the running time:'))
	theta_0 = change_amp(F,q,T)[0]
	omega_0 = change_amp(F,q,T)[1]
	t_0 = change_amp(F,q,T)[2]
	plt.plot(t_0,theta_0,'m')
	plt.text(0.7*T,0.8*max(theta_0),'$F_D=%.2f$'%F+','+'$q=%.2f$'%q,fontsize=14)
	plt.title('$\\theta$-$t$',fontsize=16)
	plt.xlabel('$t(\mathrm {s})$',fontsize=14)
	plt.ylabel('$\\theta(\mathrm {rads})$',fontsize=14)
	plt.xlim(0,1.1*T)
	plt.grid(True)	
	plt.show()
	
main()