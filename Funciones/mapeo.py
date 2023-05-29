#=======================
# Función pura x**2
#=======================
def alcuadrado(x):
    return x*x

#=======================
# Función pura x**3
#=======================
def alcubo(x):
    return x*x*x

#================================
# Mapeo de una función pura
#================================
def mapeo(func,lista_numeros):
    resultado = []

    for i in lista_numeros:
        resultado.append(func(i))
    return resultado

cuadrados = mapeo(alcuadrado,[2.5,2,3.8,1.2,6.6,1j,7,8])
cubos = mapeo(alcubo,[1,2,3,4,5,6,7,8])
print(cuadrados)
print(cubos)

#=================================
# Funciones dentro de funciones
#=================================
def en_mayusculas(texto):
    return texto.upper()

def en_minusculas(texto):
    return texto.lower()

def saludar(func):
    saludo = func("Hola, ¿qué tal?")
    print(saludo)

#===================
# Con string
#===================
saludar(en_mayusculas)
saludar(en_minusculas)

#===========================================
# Funciones abstractas dentro de funciones
# Su resultado es otra funcion
#===========================================
def divisor(x):
    def dividendo(y):
        return y/x
    return dividendo

#======================================
# Primero generamos la función y/2
#======================================
division = divisor(2)
#======================================
# La usamos para calcular 3/2
#======================================
print(division(3))

#============================================
# Uso de la funcion map con una lista
#============================================

#============================================
# Lista de ciudades y su temperatura
#============================================
temps = [ ("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angele", 26), ("Tokyo", 27), ("NUeva York", 28), ("Londres", 22), ("Pekin", 32), ("Mexico Tenochtitlan", 23)]

C_a_F = lambda datos: (datos[0], (9/5*datos[1] + 32))
print(list(map(C_a_F,temps)))

