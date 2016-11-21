import numpy as np
from visual import *
class billiard_circle:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (np.sqrt( self.x[i]**2+self.y[i]**2 ) > 1.0):
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+y**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
        
    def reflect(self,x,y,vx,vy):
        module = np.sqrt(x**2+y**2)  ### normalization
        x = x/module
        y = y/module
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*y)/v
        cos2 = (vx*y-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*y
        vy_n = vt*y-vc*x
        return vx_n,vy_n

    def Vplot(self):
        floor = box (pos=(0,0,0), length=4, height=0.3, width=4, material = materials.wood)
        ball = sphere (pos = (self.y_0,0.2,self.x_0),radius = 0.05, material = materials.marble)
        p = paths.circle(pos=(0,0,0),radius = 0.5)
        squ = shapes.rectangle(pos = (0.6,0,0),width = 0.1,height = 0.5)
        extrusion(pos=p, shape=squ, color=color.cyan)
        t = 0
        i = 0
        ball.trail = curve(color = color.white)
        while i < len(self.vx):
            rate(80)
            ball.velocity = vector(self.vy[i],0,self.vx[i])
            ball.pos = ball.pos + ball.velocity*self.dt
            ball.trail.append(pos = ball.pos)
            t = t + self.dt
            i+= 1
A = billiard_circle(0.3,0.7,0.62,0.33,3000,0.1)
A.motion_calculate()
A.Vplot()

