# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:15:04 2017

@author: Administrator
"""

import pylab as plt
import numpy as np 
import random as ra

J=1
K=1
start_temp=0.25
end_temp=5
temp_gap=0.25
step=int((-start_temp+end_temp)/temp_gap)+1

class Ising:
	def __init__(self,N):
		self.N=N
		self.t=np.linspace(start_temp,end_temp,step)
		self.s=[[1 for i in range(self.N)] for j in range(self.N)]
		self.final_E=[]
		self.final_Magnet=[]
		self.T=0.25
		
	def Cal_Energy(self):
		self.E=0
		for i in range(self.N-1):
			for j in range(self.N-1):
				self.E+=-J*(self.s[i][j]*self.s[i][j-1]+self.s[i][j]*self.s[i][j+1]+self.s[i][j]*self.s[i-1][j]+self.s[i][j]*self.s[i+1][j])

		for i in range(self.N-1):
			self.E+=-J*(self.s[self.N-1][i]*self.s[self.N-1][i-1]+self.s[self.N-1][i]*self.s[self.N-1][i+1]+self.s[self.N-1][i]*self.s[self.N-2][i]+self.s[self.N-1][i]*self.s[0][i])
			self.E+=-J*(self.s[i][self.N-1]*self.s[i+1][self.N-1]+self.s[i][self.N-1]*self.s[i-1][self.N-1]+self.s[i][self.N-1]*self.s[i][self.N-2]+self.s[i][self.N-1]*self.s[i][0])

		self.E+=-J*(self.s[self.N-1][self.N-1]*self.s[self.N-1][self.N-2]+self.s[self.N-1][self.N-1]*self.s[self.N-1][0]+self.s[self.N-1][self.N-1]*self.s[self.N-2][self.N-1]+self.s[self.N-1][self.N-1]*self.s[0][self.N-1])
		self.E=self.E/2.#/(2*(self.N**2))

		return self.E

	def scan(self):
		self.scan_E=0.
		for i in range(self.N):
			for j in range(self.N):
				self.E1=0
				self.E2=0
				self.E1=self.Cal_Energy()
				self.s[i][j]=-self.s[i][j]
				self.E2=self.Cal_Energy()
				delta_E=self.E2-self.E1
				if delta_E>0:
					p=np.exp(-delta_E/(K*self.T))
					r=ra.uniform(0,1)
					if r>=p:
						self.E3=self.E1
						self.s[i][j]=-self.s[i][j]
					else:
						self.E3=self.E2
				else:
					self.E3=self.E

				self.scan_E+=self.E3
		self.scan_E=self.scan_E/(self.N)**2
		self.temp_Magnet=0.
		for i in range(self.N):
				for j in range(self.N):
					self.temp_Magnet+=self.s[i][j]
		#return self.scan_E

	def loop(self):
		self.s=[[1 for i in range(self.N)] for j in range(self.N)]
		i=0
		self.loop_E=0.
		self.Magnet=0.
		while i<1000:
			self.scan()
			self.loop_E+=self.scan_E
			self.Magnet+=self.temp_Magnet
			i+=1
			
		self.loop_E=self.loop_E/(1000*(2*self.N**2))
		self.Magnet=self.Magnet/(1000*(2*self.N**2))
		self.final_E.append(self.loop_E)
		self.Magnet=self.Magnet/(self.N**2)
		self.final_Magnet.append(self.Magnet)
		#return self.loop_E

	
	def loop_for_temp(self):
		i=0
		for i in range(step):
			self.T=self.t[i]
			i+=1
			self.loop()

		plt.subplot(1,2,1)
		plt.plot(self.t,self.final_E,',')
		plt.title("Energy versus Tempature")
		plt.xlabel("Tempature")
		plt.ylabel("Energy per spin")

		plt.subplot(1,2,2)
		plt.plot(self.t,self.final_Magnet,',')
		plt.title("Magnetization versus Tempature")
		plt.xlabel("Tempature")
		plt.ylabel("Magnetization")

AA=Ising(10)
AA.loop_for_temp()
plt.show()