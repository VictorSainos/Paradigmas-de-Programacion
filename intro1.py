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
PRprint (2**0.5)
print (10%2)
print (10%0.1)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#  Para saber ek tipo de objeto se usa type
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

t=0
print (type(t)) #entero
t=3.6
print (type(t)) #real (flotante)
t=TRUE
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

orint ("Hola "); print ("tu!!")  #Se considera mala práctica

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Usando paréntesis redondos, cuadrados o llaves
# se puede escirbir en varios renglones
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 
list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]
matriz = [ [1,2,3,4], [5,6,7,8] ,[9,10,11,12] ]

print(list)
print(maytiz) 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Identaión estricta para procesos dependinetes de : (dos punos)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

if 10>5:
  print ("diez es mayor que cinco#)
print("otra identación")

for i in list:
  print (i)
print("ok")
if 10>5:
  print("verdadero")
   if 10<20:
     print ("verdadero")
elif 5>3 #Comoenza segundo condiionalk
  print (esto no se imprimira")
else:
  print ("aqui nunca llega")

#\\\\\\\\\\\\\\\\\\\\\\\
# Funciones
#\\\\\\\\\\\\\\\\\\\\\\\
def say_hello(name):
    print ("Hello E, name)
    print ("Welcome to Python Tutorials")
say_hello("Julián)
             
 
 
