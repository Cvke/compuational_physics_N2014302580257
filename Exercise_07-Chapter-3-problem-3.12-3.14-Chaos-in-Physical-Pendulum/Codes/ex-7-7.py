# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 07:35:10 2016

@author: Administrator
"""

import math as mt
import matplotlib.pyplot as plt

# define a function that given amplitude of force, gives theta,omega and t

def change_amp(F,q,it,T):   
    # define some constants
    l = 9.8
    g = 9.8
    f = float(2/3)
    dt = 0.04
    theta0 = it
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
	it = float(input('Please set the initial angle :'))
	T = float(input('Please set the running time:'))
	theta_0 = change_amp(F,0.5,it,T)[0]
	theta_1 = change_amp(F,0.5,it+0.001,T)[0]
	theta_2 = change_amp(F,0.55,it,T)[0]
	theta_3 = change_amp(F,0.55,it+0.001,T)[0]	
	t = change_amp(F,0.5,it,T)[2]
	delta_theta_1=[]
	delta_theta_2=[]
	for i in range(len(t)):
	   delta_theta_1.append(abs(theta_0[i-1]-theta_1[i-1]))
	   delta_theta_2.append(abs(theta_2[i-1]-theta_3[i-1]))
	plt.semilogy(t,delta_theta_1)
	plt.semilogy(t,delta_theta_2)
	plt.plot(t,delta_theta_1,'m')
	plt.plot(t,delta_theta_2,'m')
	plt.text(0.8*T,0.0001,'$F_D=%.2f$'%F,fontsize=14)
	plt.text(0.7*T,0.00001,'$q_1=0.50,q_2=0.55$',fontsize=14)
	plt.title('$\\Delta \\theta$-$t$$\,(\mathrm{with\,different\,q})$',fontsize=16)
	plt.xlabel('$t(\mathrm {s})$',fontsize=14)
	plt.ylabel('$\\Delta \\theta(\mathrm {rads})$',fontsize=14)
	plt.grid(True)	
	plt.show()
main()

