# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 01:50:38 2016

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
	theta_0 = change_amp(0,0.2,50)[0]

	t_0 = change_amp(0,0.2,50)[2]
	theta_1 = change_amp(0,0.5,50)[0]

	t_1 = change_amp(0,0.5,50)[2]
	theta_2 = change_amp(0,0.8,50)[0]

	t_2 = change_amp(0,0.8,50)[2]



	plt.plot(t_0,theta_0,label='$F_D=0.00$,$q=0.2$')
	plt.plot(t_1,theta_1,label='$F_D=0.00$,$q=0.5$')
	plt.plot(t_2,theta_2,label='$F_D=0.00$,$q=0.8$')
	plt.legend(loc='upper right',fontsize=10)
	plt.title('$\\theta$-$t$',fontsize=16)
	plt.xlabel('$t(\mathrm {s})$',fontsize=14)
	plt.ylabel('$\\theta(\mathrm {rads})$',fontsize=14)
	plt.xlim(0,1.1*50)
	plt.grid(True)	
	plt.show()
	
main()