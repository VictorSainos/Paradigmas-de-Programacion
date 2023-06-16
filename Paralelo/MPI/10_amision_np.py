from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Tamaño del areglo
n = 10
if rank == 0:
    # Arreglo de enteros del 0 al n-1
    data = numpy.arange(n, dtype='i')
else:
    # Areglo vacio de enteros de tamaño n
    data = numpy.empty(n, dtype='i')

#===============================================
# Broadcasr pro que indica el tipo de dato
# Optimizado parar cimunicacion rápida
#===============================================
comm.Bcast([data, MPI.INT], root=0)

#==================================
# Asegurarse que todo salió bien
#==================================
for i in range(n):
    assert data[i] == i
print(data)
