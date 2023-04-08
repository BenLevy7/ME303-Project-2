import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

radius = 1
time = 400

nodes_space = 60
nodes_time = 3000

dx = np.linspace(0, radius, nodes_space)
dt = np.linspace(0, time, nodes_time)
print(len(dt))
space_grid = radius/nodes_space
time_grid = time/nodes_time
alpha = 0.001

CFL = time_grid-(1/(2*alpha))*space_grid**2
print(CFL)
F = (alpha*time_grid)/(space_grid**2)
print(1-2*F)

#print(dt)

row = len(dt)   
column = len(dx)

Temp = np.zeros((row,column))

#Initial conditions
Temp[0,:] = 24

#boundary condition
Temp[:,0] = 100
Temp[:,column-1] = 100

Temp.round(2)
#print(Temp)
    
#starts at array coordinates (0,1)
#values for printing
Temp_print = []
radius_print = []
time_print = []


for i in range (1,row): #time loop
     for j in range(1,column-1): #radius loop
        Temp[i][j] =  (Temp[i-1][j]) + ((alpha*time_grid)/(radius*space_grid))*((2)*(Temp[i-1][j+1] - Temp[i-1][j]) + (radius/space_grid)*(Temp[i-1][j+1] - 2*Temp[i-1][j]+Temp[i-1][j-1]))
        #Temp[i,j] = (1-2*F)*Temp[i-1,j] + F*Temp[i-1,j+1] + F*Temp[i-1,j-1] #Regular heat equation
        #Temp[i][j] = (1-2*F)*Temp[i-1][j] + F*Temp[i-1][j+1] + F*Temp[i-1][j-1]
        #print(i,j)
        #Temp[i][j]
      




#plt.plot(np.linspace(0, 1, 100), Temp[:100, 1])
plt.plot(Temp.T)

X, T = np.meshgrid(dx,dt)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, T, Temp,cmap='hot', edgecolor='none')
ax.set_title('Surface plot')
ax.set_ylabel("Time (s)")
ax.set_xlabel("Diameter")
ax.set_zlabel("Temperature (r, t)")

plt.show()

