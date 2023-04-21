''' ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
'''
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#OPERACIONES BASICAS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

print (2+3)
print (2+3)
print (2/3)
print (2**10)
print (2**0.5)
print (10%2)
print (10%0.1)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#  Para saber ek tipo de objeto se usa type
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

t=0
print (type(t)) #entero
t=3.6
print (type(t)) #real (flotante)
t = True
print (type(t)) #boleano (bool)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Mensajes a pantalla
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

print ("Este es un comando de python. ", "Este es otr enunciado.", t)
print ('id: ', 1)
print ('First Name: ', 'Steve')
print ('Last Name: ', 'Jobs')
print ("Vamos a sumar esto" + "con esto otro")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Continuar una instrucción en varios renglones
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

if 100 > 99 and \
    200 <=300 and \
     True != False:
        print ('Hello world')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Comandos diferentes en la misma linea
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

print ("Hola "); print ("tu!!")  #Se considera mala práctica

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Usando paréntesis redondos, cuadrados o llaves
# se puede escirbir en varios renglones
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 
list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]
matriz = [ [1,2,3,4], [5,6,7,8] ,[9,10,11,12] ]

print(list)
print(matriz) 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Identaión estricta para procesos dependinetes de : (dos punos)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

if 10>5:
  print ("diez es mayor que cinco")
  print("otra identación")

for i in list:
  print (i)
  print("ok")
if 10>5:
  print("verdadero")
  if 10<20:
     print ("verdadero")
elif 5>3: #Comoenza segundo condiionalk
  print ("esto no se imprimira")
else:
  print ("aqui nunca llega")

#\\\\\\\\\\\\\\\\\\\\\\\
# Funciones
#\\\\\\\\\\\\\\\\\\\\\\\
def say_hello(name):
    print ("Hello E, name")
    print ("Welcome to Python Tutorials")
say_hello("Julián")
             
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Input permite obtener datos del usuario en prompter
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
nombre = input("Dame tu nombre: ")
print("Hola como estás",nombre)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Los enteros son de precisión ilimitada
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
y=50000000000000000000000000000000000000000000000000
print(y)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Se pueden delimitar números con guión bajo pero no con coma
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
y = 5_000_000
print(y)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# La funcion int() cambia strings y floats a enteros
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
numero = int(input("Dame tu edad: "))
type(numero)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#La notación cinetifica de flotante utiliza e o E
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#1.2 X 10^{9}
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Y = 1.2e-09
print(y)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# La funcion float() convierte strings y enteros a float
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
y = float("14.3")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Los complejos se escriben con la raíz de menos uno
# j simpre con un número prefijo
# no acepta la j suelta
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
z = 1+1j

# suma +
# resta -
# multiplicacion *
# divicion /
# módulo %
# exponente **
# // función piso
# Funciones piso para transformar números int() float() complex()
# Operadores abs()  round() pow()
           
print(round(3.14154,4))

#\\\\\\\\\\\\\\\\\\\\\\\\\\
# Strings de varias líneas
#\\\\\\\\\\\\\\\\\\\\\\\\\\
parrafo = """ En el bosque de la china
 la chinita se perdió """
print(parrafo)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# La funcion len() obtiene el tamaño del string
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
n=len(parrafo)
print(n)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Las letras en un string ocupan lugares como en un areglo
# (tambien de atras para adelante comenzando en -1 el ultimo)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
palabra = "hola"
print(palabra[0])
print(palabra[-4])

