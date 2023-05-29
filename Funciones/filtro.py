#==============================
# Uso de filtros
#==============================

#=======================================================
# Hacer una lista de los numeros por arriba del promedio
#=======================================================

# Módulo de estadistica
import statistics as sta

bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
promedio = sta.mean(bigdata)
print(promedio)

#====================================================================
# Hazme una lista de elemntos que cumplan la condicion x > promedio
# filter( condicion, datos)
#====================================================================
print(list(filter(lambda x: x > promedio, bigdata)))

#===================
# Limpiar los datos
#===================
paises = ["", "Argentina", "", "Brasil", "", "Chile", "México", "", "Colombia", "", "", "Cuba", "Venezuela"]

#=================================
# Filtrar lo que no conienen nada
#=================================
print(list(filter(None, paises)))
