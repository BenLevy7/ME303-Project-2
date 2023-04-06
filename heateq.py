import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math

radius = 1
time = 1

radius_space = 0.25
time_space = 0.25
alpha = 0.0001
F = (alpha*time_space)/(radius_space**2)

dx = np.arange(0, radius + radius_space, radius_space)
dt = np.arange(0, time + time_space, time_space)
print(dx)

row = len(dx)
column = len(dt)

Temp = np.zeros((row,column))



#Initial conditions
Temp[0,:] = np.sin(np.pi*dx)

#boundary condition
Temp[:,0] = 0
Temp[:,column-1] = 0

Temp.round(2)
#print(Temp)
    
#starts at array coordinates (0,1)

for i in range (1,row): #time loop
     for j in range(1,column-1): #radius loop
        Temp[i][j] =  (1-2*F) * (Temp[i-1][j]) + F*Temp[i-1][j+1] + F*Temp[i-1][j-1]
        #Temp [i + 1][j] = Temp [i][j] + F*(Temp[i][j+1] - 2*Temp[i][j] + Temp[i][j-1])
        #print(i,j)


#plt.plot(np.linspace(0, 1, 100), Temp[:100, 1])
plt.plot(Temp)
print(Temp)
plt.show()
