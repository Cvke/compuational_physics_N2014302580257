# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 03:48:44 2016

@author: Administrator
"""

from __future__ import division
from math import *
from pylab import *
from numpy import *

# define a function that given amplitude of force, gives angle,avelo and t

def change_amp(F):
    
	    # define some constants
	
	    q = 0.52
	    l = 9.8
	    g = 9.8
	    f = 2/3
	    dt = pi/100
	    theta0 = 0.2
	    omega0 = 0
	    angle = [theta0]
	    avelo = [omega0]
	    t = [0]
	    an=[]					
	    # move the pendulum	
	    while t[-1] <= 1200*pi:	
	        avelo_new = avelo[-1] - ((g/l)*sin(angle[-1]) + q*avelo[-1] - F*sin(f*t[-1]))*dt
	        avelo.append(avelo_new)
	        angle_new = angle[-1] + avelo[-1]*dt
	        while angle_new > pi:
	            angle_new -= 2*pi
	        while angle_new < -pi:
	            angle_new += 2*pi
	        angle.append(angle_new)
	        if t[-1]>=900*pi:
	            if t[-1]%(3*pi)<=dt:
	                an.append(angle_new)
	        t_new = t[-1] + dt
	        t.append(t_new) 
	    return an
def main():
		fd1=list(linspace(1.3,1.5,100))
		fd=[]
		th=[]	
		for i in fd1:
		    points=change_amp(i)
		    for j in points:
		        fd.append(i)
		        th.append(j)
		
		scatter(fd,th,s=7,color='r')
		grid(True)
		xlim(1.3,1.5)
		ylim(0,3.0)
		title('Bifurcation Diagram')
		xlabel('$F_D$')
		ylabel('$\\theta\\mathrm{(rads)}$')
		text(1.36,2.5,'$q=0.52')
		show()

main()

