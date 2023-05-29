#==========================================
# Uso de reducciones (colapsar resultados)
#==========================================

#===============================================
# Multiĺicación de todos los númerps en la lista
#===============================================

from functools import reduce

bigdata = [2,3,5,7,11,13,19,23,29]

#==================
# Función x*y
#==================
multiplicar = lambda x,y:x*y

print(reduce(multiplicar, bigdata))

#==========================================================
# Reduce le aplica la funcion por pares a los resultados
# el siguiente elemento comenzando con los dos primeros
# elementos
#==========================================================
