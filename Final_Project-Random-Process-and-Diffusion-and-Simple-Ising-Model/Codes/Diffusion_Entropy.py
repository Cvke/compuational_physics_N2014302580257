# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:48:50 2017

@author: Administrator
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import random

N=100
accuracy=1e-10
class Fields:
	def __init__(self,step):
		self.v=[]
		self.Entropy=[]
		self.step=step
		self.old_v=[]
		for i in range(N):
			self.v.append([])
			self.old_v.append([])

		#print len(self.old_v)

		for i in range(N):
			for j in range(N):
				self.v[i].append(0)
				self.old_v[i].append(0)

		for i in range(25,75):
			for j in range(25,75):
				self.v[i][j]=1

	def update(self):
		s=0
		global temp_Entrpy
		temp_Entropy=0
		self.Delta_v=0.
		for i in range(N):
			self.v[i][0]=0
			self.v[i][N-1]=0

		for j in range(N):
			self.v[0][j]=0
			self.v[N-1][j]=0

		for i in range(N):
			for j in range(N):
				self.old_v[i][j]=self.v[i][j]


		for i in range(1,N-1):
			for j in range(1,N-1):
				self.v[i][j]=(self.old_v[i+1][j]+self.old_v[i-1][j]+self.old_v[i][j+1]+self.old_v[i][j-1])/4.
				s+=self.v[i][j]

		for i in range(N):
			for j in range(N):
				if (self.v[i][j]!=0):
					temp_Entropy+=-(self.v[i][j]/s)*np.log(self.v[i][j]/s)

		self.Entropy.append(temp_Entropy)

	def fire(self):
		counter=0
		for i in range(self.step):
			self.update()
			counter+=1
			i+=1

		plt.plot(np.linspace(1,self.step,self.step),self.Entropy,linewidth=2)
		return self.v


Super=Fields(2000)
Super.fire()
plt.xlabel("step number n")
plt.ylabel("Entropy of the system")
plt.title("Entropy of the two dimension system vary over 2000 steps")
plt.show()