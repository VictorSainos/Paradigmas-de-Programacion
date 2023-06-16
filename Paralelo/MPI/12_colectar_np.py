from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 10

#===============================================
# Arreglo de ceros de tamaño n
# sumando con un escalar (en cada entrada)
#===============================================
sendarray = numpy.zeros(n, dtype='i')+rank

recvarray = None

if rank == 0:
    #==========================================
    # Matriz vacía para numpy
    # dtype es el tipo de dato (i) es entero
    #==========================================
    recvarray = numpy.empty([size, n], dtype='i')

#==============================
# Gather es rápido para numpy
# enviar datos al proceso root
#==============================
comm.Gather(sendarray, recvarray, root=0)

if rank == 0:
    for i in range(size):
        #===========================================================
        # Revisa por fila la matrix
        # : significa todos los elemntos de esa dimensión
        # allclose es un método de numpy que compara los elmenos
        #===========================================================
        assert numpy.allclose(recvarray[i,:], i)

print(recvarray)

