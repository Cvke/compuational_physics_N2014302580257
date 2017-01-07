# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:14:33 2017

@author: Administrator
"""

import pylab as plt
import numpy as np 
import random as ra

J=1
K=1
class Ising:
	def __init__(self,N,t):
		self.N=N
		self.T=t
		self.s=[[1 for i in range(self.N)] for j in range(self.N)]
		self.final_E=[]
		self.final_Magnet=[]
		self.time=[]
	
	def Cal_Energy(self):
		self.E=0
		for i in range(self.N-1):
			for j in range(self.N-1):
				self.E+=-J*(self.s[i][j]*self.s[i][j-1]+self.s[i][j]*self.s[i][j+1]+self.s[i][j]*self.s[i-1][j]+self.s[i][j]*self.s[i+1][j])

		for i in range(self.N-1):
			self.E+=-J*(self.s[self.N-1][i]*self.s[self.N-1][i-1]+self.s[self.N-1][i]*self.s[self.N-1][i+1]+self.s[self.N-1][i]*self.s[self.N-2][i]+self.s[self.N-1][i]*self.s[0][i])
			self.E+=-J*(self.s[i][self.N-1]*self.s[i+1][self.N-1]+self.s[i][self.N-1]*self.s[i-1][self.N-1]+self.s[i][self.N-1]*self.s[i][self.N-2]+self.s[i][self.N-1]*self.s[i][0])

		self.E+=-J*(self.s[self.N-1][self.N-1]*self.s[self.N-1][self.N-2]+self.s[self.N-1][self.N-1]*self.s[self.N-1][0]+self.s[self.N-1][self.N-1]*self.s[self.N-2][self.N-1]+self.s[self.N-1][self.N-1]*self.s[0][self.N-1])
		self.E=self.E/2.

		return self.E

	def update(self):
		self.E1=self.Cal_Energy()
		chosen_x=ra.randint(0,self.N-1)
		chosen_y=ra.randint(0,self.N-1)
		self.s[chosen_x][chosen_y]=-self.s[chosen_x][chosen_y]
		self.E2=self.Cal_Energy()
		delta_E=self.E2-self.E1
		if delta_E>0:
			p=np.exp(-delta_E/(K*self.T))
			r=ra.uniform(0,1)
			if r>=p:
				self.E3=self.E1
				self.s[chosen_x][chosen_y]=-self.s[chosen_x][chosen_y]
			else:
				self.E3=self.E2
		else:
			self.E3=self.E

	def cal_Magneti(self):
		self.Magnet=0.
		for i in range(self.N):
			for j in range(self.N):
				self.Magnet+=self.s[i][j]

		return self.Magnet

	def loop(self):
		self.ave_Magnet=0.
		self.s=[[1 for i in range(self.N)] for j in range(self.N)]
		i=1
		while i<=1000:
			self.update()
			self.ave_Magnet+=self.cal_Magneti()
			i+=1
			#print i

		self.ave_Magnet=self.ave_Magnet/(1000*self.N**2)
		self.final_Magnet.append(self.ave_Magnet)

	def draw(self):
		i=0
		while i<=1000:
			self.loop()
			self.time.append(i)
			i+=1

		plt.plot(self.time,self.final_Magnet,label="Tempature"+str(self.T)+"K")


A=Ising(10,1.0)
A.draw()
A=Ising(10,2.0)
A.draw()
A=Ising(10,3.0)
A.draw()
A=Ising(10,4.0)
A.draw()
plt.xlabel("Times(number of step")
plt.ylabel("Magnetization")
plt.legend(loc="best")
plt.title("Ising_Model_Magnetization_Versus_Time(steps)")
plt.show()