from Exponencial import expon

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
 
lista = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]
matriz = [ [1,2,3,4], [5,6,7,8] ,[9,10,11,12] ]

print(lista)
print(matriz) 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Identaión estricta para procesos dependinetes de : (dos punos)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

if 10>5:
  print ("diez es mayor que cinco")
  print("otra identación")

for i in lista:
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

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Conjunto en python 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
even_nums = {2, 4, 6, 8, 10}  #conjunti de números pares
print (even_nums)

#El bool no es parte del conjunto
emp = {1, 'Steve', 10.5, True} # conjunto de diferentes objetos
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Convertir secunecias a conjuntos
# No lo genera en orden
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
s = set((1,2,3,4,5)) # tupla a conjunto
print(s)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# De diccionario a conjunto: conjunto de llaves
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
d = {1: 'One', 2: 'Two'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums) 
print(s)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

su = s1|s2 #Unión
print(su)

si = s1&s2 # intersección
print(si)

sr = s1-s2  # Dieferencia de conjuntos
print(sr)
ss = s1^s2 # Diferencia simetrica
print(ss)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Usi de diccionarios
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
capitals = {"USA":"Washington D.C", "France":"Paris", "India":"New Delhi"}
print(capitals)
 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\                     
# Llave:valor
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# diccionario vacio
d={}

# llaveentera, valor string
numNames={1:"One", 2:"Two", 3:"Three"}

#Llave real, valor string"}
decNames={1.5:"One and Half", 2.5:"Two and Half", 3.5:"Three and Half"}

# Lave tipla, valor string 
items={ ("Parker", "Reynolds", "Camlin"):"pen", ("LG", "Whirlpool", "Samsung"): "Refrigerator"}

# Llave string, valor int  
romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

# Reportar llave y valor
for k in capitals:
    print("Key =" + k +  ", Value = " + capitals[k])

# Nuevo dato para eldiccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato dl diccionario
del capitals["Mexico"]
print(capitals)

# Borrar todo el dicionario
del capitals

# Reportar llaves
print(romanNums.keys())

# Reportar valores
print(romanNums.values())

# Juicio de llaves (está o no esta la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" in romanNums)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  
# LISTAS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Listas
# Las listas pueden ser de objetos diferentes
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
miprimeralista = [] # Lita vacia
print(miprimeralista)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Llenado de listas
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
miprimeralista = {1,"Javier",1.34,"Bosco","Angel","Abigail",True}
print(miprimeralista)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# list: hacer una lista
# range(i,j): secunacia de i hasta j-1
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
nums = list(range(1,61))

for i in nums:
    print(i)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Incluir nuevos elemntos en la lista
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)
                                             
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Quitar elemntos de la lista
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
i = 61
del nums[i]
print(nums)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Borrar lista
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
del nums

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Sumar listas 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
L1=[1,2,3]
L2=[4,5,6]
print(L1+L2)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Llenado a mano
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
potencial = []
for i  in range(0,10000):
    potencial.append(float(i))
print(potencial[100])
            
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Generar una tupla con la lista
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
potencial = tuple(potencial)
print(potencial[100])


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Condicionales
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
precio = 50
#------------
# Si esto...
#-----------
if precio < 50:
    print("El precio es menor que 50")
#--------------------------
# Si no...si esto otro....
#---------------------------
elif precio >50:
    print("El precio es mayor a 50")
#-----------------------------
# Si nada de lo anterior
#------------------------------
else:
    print("El precio es 50")
precio = 50
cantidad = 5
total = precio*cantidad
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Comdiciomales anidados
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor que 400")
        elif total < 500 and total >300:
            print("Total emtre 300 y 500")
        else:
            print("Total entre 100 y 300")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Condicional de igualdad son ==
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
elif total == 100:
   print("Total es 100")
else:
    print("Total menor que 100")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Contador mientras la condicion sea verdadera
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
num = 0
while num < 5:
    num = num+1
    print('num =', num)

num = 0
while num < 5:
    num+=1                     # num +=1 es lo mismo que num = num+1
    print('num =', num)        # cindicionantes de salir del bluque
    if num == 3:
        break

num = 0
while num < 5:
    num+=1
    if num < 3:
        continue               # evita lo que sigue, continiar con las iteraciones
    print('num =', num)

#\\\\\\\\\\\\\\\\\\\\
# Bucle sobre lista
#\\\\\\\\\\\\\\\\\\\\
nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Bucle sobre un string
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
for char in 'Hello':
    print(char)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Bucle sobre un diccionario
# intem = elementos
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
numNames = { 1:'One',2:'Two', 3:'Three'}
for pair in numNames.items():
    print(pair)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # Bucle sobre diciconario
# key = llave
# value = valor
for k,v in numNames.items():
    print("Key = ", k, ", value =", v)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Primera función
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def saludo():
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Documentación rápida de la función
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    """Esta funcion saluda"""
    print('¡Quiúboles!, ¿cómo estas?')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Llamado de la función
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
saludo()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Se ejecuta pero no se aigna
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
salida = saludo()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Mostrar documentación
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#help(saludo)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Función con argumento
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print("¡Qué onda ese",nombre,"!")
salu2("Julián")
salu2("Ángel")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Ahorrar trabajo del intérprete
# nombre:str la variable nombre es un str
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def saludos(nombre:str):
    """ ESta función te saluda por tu nombre estrictamente"""
    print("¡Qué onda ese ",nombre,"!")
saludos("Julián")
a=123
print(type(a))
saludos (a)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Función con muchos argumentos
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def saludos_multiples(nombre1, nombre2, nombre3):
    """ Esta funcion saluda a 3 personsa al mismo timepo"""
    print("Hola",nombre1, ",", nombre2,"y",nombre3)
saludos_multiples("Hugo", "Paco", "Luis")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Función con cualquier número de argumentos
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def muchos_saludos(*nombres):
    """ ESta función saluda a todos los que queiras"""
    i=0
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # end = es para ponerlo de corrido
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    print("Hola", end="")
    while len(nombres) > i:
        # Último nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
        # Cualquier otro nombre
            print(nombres[i-1], end="")
        i+=1

muchos_saludos("Bosco","Angel", "Davidad","Tamara","Mili","Edwin","Lev","Luis","Abigail")

def greet(firstname, lastname):
    print('Hello', firstname, lastname)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Llamar a la función con argumentos en desorden
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
greet(lastname='Jobs', firstname='Steve') # Se peuden especificar en desorden

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Función con argumentos escondidos **
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def greet(**person):
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # persona tiene caracteristicas firstnaem y lastname
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    print('Hello', person['firstname'], person['lastname'])

greet(firstname='steve', lastname='Jobs')
greet(lastname='Jobs', firstname='Steve')
greet(firstname='Bill', lastname='Gates', age=55) #Se pueden pasar mas parametros de los necesarios

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Función con valores por defecto
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def greet(name ='guest'):
    print('Hello', name)

greet() # Utiliza el valor dado de antemano
greet('Steve')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Función con resultado
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def suma(a,b):
    return a+b

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Programación funcional
# Se pueden funciones en funciones
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
total = suma(5, suma(10,20))
print(total)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Calculo lambda
# nombre de la funcion = lambda variable : función
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
x_al_cuadrado = lambda x: x * x
a1 = x_al_cuadrado(5)
print(a1)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Lambda de varias variables
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
suma = lambda x1, x2, x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]

print(sumas(100,200,300,400))

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Uso de una función anónima
# El argumento va afuera entre paréntesis
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print((lambda x: x*x)(6)) # Función anónima

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Función con  variables global
# EVITE EL EXCESO !!!!
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
name = 'Steve'
def greet():
    global name  # Para utilizar una variable global (que viene fuera del bloque
    name = 'Bill'
    print('Hello', name)

greet()


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Algoritmo 1
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

expon(-100,200)
