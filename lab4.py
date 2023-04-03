#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# PROGRAMACIÓN OIENTADA A OBJETO
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#|||||||||||||||||||||||||||||||||
# Una clase para un objeto vacío
# No está tan vacpio, necesita
# la palabra pass = pasar
#|||||||||||||||||||||||||||||||||
class ObjetoVacio:
    pass

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# nada es un ObjetoVacio
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
nada = ObjetoVacio()
print(type(nada))

#=================
# La clase llanta
#=================
class Llanta:
    #==================================
    # Variable cuneta es toda la clase
    #==================================
    cuenta=0
    #====================================
    # Función constructora de identidad
    # __init__ es una función reservada
    # comienza con uno mismo: self
    # pero puede ser otro nombre
    # parámetros de entrada = default
    #====================================
    def __init__(mi,radio=50,ancho=30,presión=1.5)
        # variable de la estructura completa Llanta
        Llanta.cuenta +=1
        # variable exclusiva de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión

#============================================
# Objetos (instanciados)
#============================================
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presión=1.2)
llanta3 = Llanta()
llanta4 = Lalanta(40,30,1.6)

#===========================================
# Objeto que contiene otros objetos
#===========================================
class coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llante3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ",Llanta.cuenta) # Variable gloal de la clase
print("Presión de la llanta 4 = ",llanta4.presión) # Presión de la llanta 4
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ",llanta3.radio)
print("Presión de la llanta 1 de i coche = ", micoche.llanta1.presión)

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# Encapsulamiento
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#=====================================================================
# Uso de la función de python property para poner y obtener atributos
#======================================================================
class EStudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi, nombre):
        print('se llamó a ponerme_nombre')
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print('se llamó a obtener_nombre')
        return mi,__nombre
    nombre=property(obtener_nombre,ponerme_nombre)

#======================================
# Crear objetos estudainte sin nombre
#======================================
estudiante = Estudiante()

#=====================================================================
# Ponerle nombre usando la propiedad nombre y el método ponerme_nombre
# (sin tener que llamar explícitamente la función
#=====================================================================
estudiante.nombre = "Diego"

#======================================================================
# Obtener el nombre con el método obtener_nombre
# __nombre es una variable encapsulada (no visible desde fuera)
# (sin tener que lalmar explicitamente a la función obtener_nombre)
#======================================================================
print(estudiante.nombre)

# Esto no funciona
#print(estudiante.__nombre)

#/\/\/\/\/\/\/\/\/\/\/\/\
# Herencia de clases
#/\/\/\/\/\/\/\/\/\/\/\/\
class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

        def perimetro(mi):
            p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
            print("perimetro=",p)
            return p

#===============================================
# Su hijo rectangulo
# Rectangulo es hijo de cuadrilatero
# Rectangulo(Cuadrilatero)
#===============================================
