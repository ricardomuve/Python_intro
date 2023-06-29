# -*- coding: utf-8 -*-
"""
## Tuplas
Created on Thu Jun 29 11:47:46 2023
@author: PILARES
"""

## Tuplas heterogéneas
t_nombre = (1,2,3,4,"Poo","Java")
print("Contenido de tupla: ")
print(t_nombre)
print("Longitud =", len(t_nombre))

max(t_nombre)
print(t_nombre[-1])

tupla_zero = (3,4,5,6,7,8,9,9,10)
print(tupla_zero[3:])

## Método len() para saber el tamaño de mi tupla
frutas = ("sandía","papaya","mango","fresa","naranja")

## Rango: 0 a len(frutas)
for i in range(0,len(frutas)):
    print(frutas[i])

## Ciclo for tiene por default '0' como inicio de iteración
for i in range(5):
    print(frutas[i])
    
for i in range(0,5):
    print(frutas[i])

## Otro método para imprimir Tuplas:
for i in frutas:
    print(i)
    
carros = ("chevy","VW","Nissan")
letras = ('a','b','d','c')
numeros = (1,4,3,8,5,2)

## Método sorted: ordena la tupla
sorted(letras)
sorted(carros)
sorted(numeros)

    
    
    
   
    
    
    