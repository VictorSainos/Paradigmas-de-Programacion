#=================================
# Curvas Z-spline en n dimeciones
#=================================
import numpy as np
from Curva import Curva,zspline
import matplotlib.pyplot as plt
import math

#=====================
# Conjuntos de puntos
#=====================
#Números de puntos
nump:np.int32 = 8
# Dimensión
dim:np.int32 = 2
# Memoria para puntos
puntos = np.zeros(dim*nump,dtype=np.float64)
#Parametrizcion
X = np.linspace(0.0,2*np.pi,nump+1)
# Coordenada x
puntos[0:nump] = np.cos(X[0:nump]) + 0.0*np.sin(2*X[0:nump])
# Coordenada y
puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

#============================================================
# CUrva Z-spline de n puntos zspline(p.d,n,m)
# p: puntos, d: dmension, n: segmentos de curva, m: continuidad
#================================================================
n:np.int32 = 1000
x1,y1 = zspline(puntos,dim,n,2)
x2,y2 = zspline(puntos,dim,n,1)
x3,y3 = zspline(puntos,dim,n,0)
plt.plot(x3,y3,lw=2,color="orange")
plt.plot(x2,y2,lw=2,color="red")
plt.plot(x1,y1,lw=2,color="blue")
plt.scatter(puntos[0:nump],puntos[nump:2*nump],marker="o",color="black")
plt.xlabel( "Coordenada x")
plt.ylabel(" Coordenada y")
plt.title("Curva cerrada Z-spline en 2D")
plt.show()
