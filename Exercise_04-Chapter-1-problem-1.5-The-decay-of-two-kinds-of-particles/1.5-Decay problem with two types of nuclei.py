# -*- coding: utf-8 -*-
"""
Decay problem with two types of nuclei
@author: Chenducvke
"""

import matplotlib.pyplot as pl
import math
MAX = 100

def initialize(nuclei_a,nuclei_b,t):
    nuclei_a[0]=float(input('initial number of N_a:'))
    nuclei_b[0]=float(input('initial number of N_b:'))
    tc_a=float(input('time constant for particle_a:'))
    tc_b=float(input('time constant for particle_b:'))
    dt=float(input('time step:'))
    t[0]=0.0
    return nuclei_a,nuclei_b,t,tc_a,tc_b,dt


def calculate(nuclei_a,nuclei_b,true_a,true_b,t,tc_a,tc_b,dt):
    alpha = tc_b/tc_a
    A = (nuclei_a[0]*alpha-nuclei_b[0])/(alpha+1)
    B = (nuclei_a[0]+nuclei_b[0])/(alpha+1)
    for i in range(MAX-1):
        nuclei_a[i+1] = nuclei_a[i] + ((nuclei_b[i]/tc_b)-(nuclei_a[i]/tc_a))*dt
        nuclei_b[i+1] = nuclei_b[i] + ((nuclei_a[i]/tc_a)-(nuclei_b[i]/tc_b))*dt
        true_a[i+1] = A*math.exp(-t[i]*(tc_b/tc_a+1)/tc_b)+B
        true_b[i+1] = -A*math.exp(-t[i]*(tc_b/tc_a+1)/tc_b)+B*alpha
        t[i+1] = t[i]+dt
    return nuclei_a,nuclei_b,true_a,t
    
def store(nuclei_a,nuclei_b,t):
    data = open('data.txt','w')
    for i in range(MAX):
        data.write(str(t[i]))
        data.write(' ')
        data.write(str(nuclei_a[i]))
        data.write(' ')
        data.write(str(nuclei_b[i]))
        data.write('\n')
    data.close
    
def draw_figure(nuclei_a,nuclei_b,True_A,True_B,t,tc_a,tc_b,dt):
    pl.figure(figsize=(10,6),dpi=144)
    pl.plot(t,True_A,'r',label='$N_A$(true)')
    pl.plot(t,nuclei_a,'m*',label = '$N_A$(numerical)')
    pl.plot(t,True_B,'b',label='$N_B$(true)')
    pl.plot(t,nuclei_b,'co',label = '$N_B$(numerical)')
    pl.xlabel('Time(s)')
    pl.ylabel('Number of Nuclei')
    pl.text(0.7*dt*MAX,0.1*nuclei_a[0],'Time Constant(A) ='+str(tc_a)+'s'+'\n'+'Time Constant(B) ='+str(tc_b)+'s'+'\n'+'Time Step ='+str(dt)+'s')
    pl.legend(loc = 'upper right',fontsize = 8)
    pl.savefig('chapter1-1.5.png',dpi=144)
    pl.title('Decay problem with two types of nuclei')
    pl.show()
    
        
def main():
    n_a = [0]*MAX
    n_b = [0]*MAX
    t = [0]*MAX
    true_a=[0]*MAX
    true_b=[0]*MAX
    (n_a,n_b,t,tau_a,tau_b,dt)=initialize(n_a,n_b,t)
    true_a[0] = n_a[0]
    true_b[0] = n_b[0]
    calculate(n_a,n_b,true_a,true_b,t,tau_a,tau_b,dt)
    store(n_a,n_b,t)
    draw_figure(n_a,n_b,true_a,true_b,t,tau_a,tau_b,dt)
    
main()