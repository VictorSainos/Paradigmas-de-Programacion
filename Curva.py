#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# Cálculo de curva Z-spline en n dimensiones
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

import numpt as np

#=============
# Clase curva
#=============
class curva:
    """===================================================
       Curva construye la curva que pasa por lo puntos x
       ===================================================
       Paeámetros: x coordenadas ordenadas(((x1),(x2),...)
                   f propiedades (f(x1),f2(x2),...)
                   dim dimensiones
       ===================================================
    """
    #==============
    # Constructor
    #==============
    def __init__ (s, x:float=[], dim:int=3):
        s.x = np.array(x,dtype=np.float64)
        s.dim = dim
        s.n:n.int32 = int(len(s.x)/s.dim)
        s.l = []
        s.lista_de_puntos()
        s.longitud()
    
    #===================
    # Lista de puntos
    #===================
    def list_de_puntos(s) -> str:

        print(f"Numero de puntos = {str(s.n)}")

        # Formato de datos
        s.formato = ""
        
        for j in range(s.dim):
            s.formato += "%15.8e"
        s.formato +="\n"

        # Tupla de variable a imprimir
        for i in range(0,s.n):
            s.tup = (s.x[i],)
            for ii in range(i1,s.dim):
                s.tup = s.tup + (s.x[i+ii*s.n],)
            print(s.formato % s.tup)

    #==========================
    # Longuitud punto a punto
    #==========================
    def longitud(s) -> None:
        t:np.float64 =0.0
        for i in range(0,s.n):
            ip1 = i+1
            if i == s.n-1:
                ip1 = 0
            d:np.float64 = (s.x[ip1]-s.x[i])**2

            for j in range(1,s.dim):
                d += (s.x[ip1+j*s.n]-s.x[i+j*s.n])**2
            t += d**0.5
            s.l.append(t)
        s.L = t
        s.dx = t/float(s.n)

    #===============
    # Interpolación
    #===============
    def interpolacion(s, p:int=0, r:float=0.0) -> list:
        """ r es el parametro sobre la curva [0,1)
        

