from datetime import datetime, date, time, timedelta

import calendar
print ("=======================================")
print ("=       programa for vs while         =")
print ("=======================================")
print ("este programa pide al usuario qué elemento quiere que busquemos")
print ("y cuando lo encuentre que lo sustituya por otro elemento")
lista1=[]
lista2=[]
numelem=int(input("dime el número de elementos que quieres que tenga la \
lista: "))
for i in range(numelem):
    lista1.append(i)
    lista2.append(i)
       

sustituir=int(input("dime qué elemento quieres sustituir: "))
newelem=int(input("dime qué nuevo elemento quieres poner en su lugar: "))

h1 = datetime.now()

for i in range(len(lista1)):
    if lista1[i]==sustituir:
        lista1[i]=newelem
h2 = datetime.now()
resultado1 = h2 - h1
print ("el bucle for ha tardado: ",resultado1)

h3 = datetime.now()
while sustituir in lista2:
    lista2[lista2.index(sustituir)]=newelem
h4 = datetime.now()
resultado2 = h4 - h3
print ("el bucle while ha tardado: ",resultado2)    

"""conclusión: un WHILE se puede escribir en forma de FOR, y viceversa, pero:
1)cuando sabemos de antemano que lo vamos a recorrer un número N determinado
de veces (aunque estas N veces puede que sea variable en cada ejecución, pero sabemos
que hay N iteraciones, realizamos un FOR)
2)cuando NO sabemos de antemano las iteraciones que vamos a realizar, ya que éstas
depende de una condición se usa un WHILE
3)si un problema lo debemos resolver con un FOR y lo hacemos con un WHILE, el coste
computacional es el mismo, pero utilizamos el FOR que para eso está
4) cuando un problema lo debemos resolver con WHILE, y lo hacemos con un FOR, el coste
computacional varía(que es el caso de este ejemplo), y dependerá del tamaño del
problema a resolver para el que se aprecie más o menos la diferencia en cuanto a coste
computacional."""