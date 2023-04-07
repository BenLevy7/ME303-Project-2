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
time = 1

radius_space = 0.01
time_space = 0.01
alpha = 0.001
F = (alpha*time_space)/(radius_space**2)

dx = np.linspace(0, radius, 10)
dt = np.linspace(0, time, 10)
print(dx)

row = len(dx)   
column = len(dt)

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
        Temp[i][j] =  (Temp[i-1][j]) + ((alpha*time_space)/radius)*((2/radius_space)*(Temp[i-1][j+1] - Temp[i-1][j]) + (radius/radius_space**2)*(Temp[i-1][j+1] - 2*Temp[i-1][j]+Temp[i-1][j-1]))
        #Temp[i,j] = (1-2*F)*Temp[i-1,j] + F*Temp[i-1,j+1] + F*Temp[i-1,j-1]
        #Temp[i][j] = (1-2*F)*Temp[i-1][j] + F*Temp[i-1][j+1] + F*Temp[i-1][j-1]
        #print(i,j)
        #Temp[i][j]
      




#plt.plot(np.linspace(0, 1, 100), Temp[:100, 1])
plt.plot(Temp.T)
#print(Temp)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(dx, dt, Temp,cmap='hot', edgecolor='none')
ax.set_title('Surface plot')

plt.show()

