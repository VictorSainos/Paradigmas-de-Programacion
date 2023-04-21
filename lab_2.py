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
nums = list(range(1,6))

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
    potencial.appendfloat(i)
print(potencial[100])
            
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Generar una tupla con la lista
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
potencial = tuple(potencial)
print(potencial[100])

