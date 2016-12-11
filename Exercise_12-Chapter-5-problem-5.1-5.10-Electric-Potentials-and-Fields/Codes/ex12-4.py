from __future__ import division
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# initialize the grid

grid = []
for i in range(41):    
    row_i = []
    for j in range(41):
        if i == 0 or i == 40 or j == 0 or j == 40:
            voltage = 0
        elif i==20 and j==20:
            voltage = 1
        else:
            voltage = 0
        row_i.append(voltage)
    grid.append(row_i)

# define the update_V function (Gauss-Seidel method)

def update_V(grid):

    delta_V = 0

    for i in range(41):    
        for j in range(41):
            if i == 0 or i == 40 or j == 0 or j == 40:
                pass
            elif i==20 and j==20:
                pass
            else:
                voltage_new = (grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
                voltage_old = grid[i][j]
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new

    return grid, delta_V

# define the Laplace_calculate function

def Laplace_calculate(grid):

    epsilon = 10**(-5)*200**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 10:
        grid_impr, delta_V = update_V(grid_init)
        grid_new, delta_V = update_V(grid_impr)
        grid_init = grid_new
        N_iter += 1

    return grid_new

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

x = np.linspace(0,40,41)
y = np.linspace(0,40,41)
X, Y = np.meshgrid(x, y)
Z = Laplace_calculate(grid)


plt.figure()
CS = plt.contour(X,Y,Z,10)
plt.clabel(CS, inline=1, fontsize=12)
plt.title('Voltage near point charge')
plt.xlabel('x')
plt.ylabel('y')

fig = plt.figure()
ax = fig.gca(projection='3d')
surf=ax.plot_surface(X, Y, Z,rstride=1, cstride=1,cmap = cm.coolwarm_r,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.0, 1.0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Voltage(V)')
ax.set_title('Voltage distribution')

plt.show()