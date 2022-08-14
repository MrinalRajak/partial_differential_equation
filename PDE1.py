
#simple Nummerical Laplace's equaion solution using finite method

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#set maximum iterations

maxIter=500
#set dimmention and the delta
lenx=75
leny=75
delta=1 #we set it square/rectangular
#Boundary conditions
Ttop=75.0
Tbottom=30.0
Tleft=10.0
Tright=0.0
#Initial gauss interior grid
Tgauss=30.0
#set meshgrid
X,Y=np.meshgrid(np.arange(0,lenx),np.arange(0,leny))
#set array size and the interior value with Tgauss
T=np.empty((lenx,leny))
T.fill(Tgauss)
#set boundary condition
T[0,:]=Tbottom
T[:,0]=Tleft
T[-1,:]=Ttop
T[:,-1]=Tright
print(T)
#Error to be stored
E=[]
#Iteration (here we assume that 'T' converges in maxIter=500)
for iteration in range(0,maxIter):
    To=T.copy()
    for i in range(1,lenx-1,delta):
        for j in range(1,leny-1,delta):
            T[i,j]=0.25*(T[i+1,j]+T[i-1,j]+T[i,j+1]+T[i,j-1])
    err=np.sum(T-To)**2
    E.append(err)
plt.title("Error as a function of iteration")
Niter=range(maxIter)
plt.plot(Niter,E,color='black')
plt.xlabel('Number of iterations')
plt.ylabel('Error')
plt.grid(True)
plt.show()

print(T[i,j])
#configure the contour
plt.title('contour of temperature')
plt.contour(X,Y,T,colors='black')
plt.contourf(X,Y,T) # Filled contour in color scale
#set color bar
plt.colorbar()
plt.show()
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,T,cmap='gist_heat_r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Temperature(T)')
plt.show()

















































