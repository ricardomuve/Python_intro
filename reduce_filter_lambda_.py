# -*- coding: utf-8 -*-
"""

Created on Thu Jul 13 11:25:17 2023
@author: PILARES
"""



## Si es string ##########################################################################
def palabra(frase):   
    # Método isaplha()
    while not frase.isalpha():
        print("El valor debe ser un texto.")
        frase=input("Ingresa un texto: ")
            
    
frase=input("Ingresa un texto")
palabra(frase)

## Si es número ##########################################################################

# No tiene un parámtero
def numero():
    while True:
        entrada=input("escribe un número entero: ")
        
        # try/catch validación en funciones
        try:
            #casteo de str --> int
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("La entrada es incorrecta: Escribe un número. ")

numero()


## Funciones Recursivas ##########################################################################

#*** Potencia ***************************
def potencia(a,b):
    if a**b>1000:
        return a**b
    print(a**b)
    potencia(a,b+1)
    

potencia(2,2)



## Funciones anónimas (lambda)  ##########################################################################

#*** Serie de fibonacci ***************************

def fibonacci(index):
    if index==0 or index==1:
        return 1
    return fibonacci(index-1) + fibonacci(index-2)


fibonacci(2)
fibonacci(0)


#**************************************************
operacion = lambda x:x+10
operacion(5)

prod = lambda x,y:x*y
prod(5,10)



# Ejercicio:
##  Usando lambda, apliquemos filter para quedarnos
##  con los números múltiplos de '7'

lista = [49,57,62,147,2101,22]

list(filter(lambda x:(x%7==0),lista))


#************************
lista2 = [49,57,62,147,2101,22]

val = lambda x:(x%7==0)

## list() convierte en lista
## filter() selecciona elementos que cumplan con argumento 
list( filter(val,lista2) )

#************************
def frase(palabra):
    return palabra[2]=="s"

palabras = ["saturno","java","python","masa","tostada","saturno"]

list(filter(frase,palabras))
    
    
    
    
## Función reduce ##########################################################################
## Factorial desde una lista.

# Importamos la biblioteca y el método
from functools import reduce

# Definimos lista
num = [1,2,3,4,5,6]

num2 = [1,2,3,4,5]

#llamamos el método junto con una lambda
reduce(lambda x,y:x*y,num)

reduce(lambda x,y:x*y,num2)

#************************

def ejemplo(a,b):
    
    if a>b:
        return a
    return b

#Devuelve el mayor entre 2 números
#ejemplo(5,8)
numeros = [-10,5,7,-3,-30,2]

#Devuelve el mayor de la lista
reduce(ejemplo,numeros)



















