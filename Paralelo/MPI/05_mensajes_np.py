#===============================================
# Uso de MPI optimizado para cálculos numéricos
#===============================================
from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self,rank):
        #===============================
        # Areglo de numpy (optimizado)
        #===============================
        self.x = np.array([float(x+rank) for x in range(10)])
        self.p = "vengo del proceso "+str(rank)

#======================
# Programa principal
#======================
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dst = rank+1 if rank!=size-1 else 0

    #========================
    # Areglo para enviar
    #========================
    m = s.x
    #print(m)
    #=====================================
    # Isend Irecv so  para comunicación
    # no bloquante de arreglos de numpy
    #=====================================
    comm.Isend(m, dest=dst)

    #=============================================
    # Arreglo vacio para recibir
    # con dimension 10 y tipo de datos
    # float64 (doble precisión)
    #=============================================
    a = np.zeros(10,dtype=np.float64)
    req = comm.Irecv(a, source=src)
    req.Wait()
    print("Soy el proceso ",rank,",el resultado es ", a)
