# -*- coding: utf-8 -*-
"""
## Listas
Created on Tue Jun 27 11:36:06 2023
@author: searchman
"""
## Creamos lista
lista2=["python","c++","C","Java","Pascal"]

## indice por default: 0
print(lista2)
print("")

## Imprimiendo lista hasta cierto índice
print(lista2[:1])
print(lista2[:2])
print(lista2[:3])
print(lista2[:4])
print(lista2[:5])
print(lista2[:20])
print("")

## Imprimiendo lista desde cierto índice
print(lista2[0:])
print(lista2[1:])
print(lista2[2:])
print(lista2[3:])
print(lista2[4:])
print(lista2[5:])
print(lista2[20:])

## Imprimiendo todos menos el último
print(lista2[:-1])
## otra manera:
print(lista2[:4])

## Imprimiendo lista desde el índice m=1 hasta n=3
print(lista2[1:3])

## Cambiando todos los valores de mi lista
lista2[0:5]=[1,2,3,4,5]
print(lista2)

## Lista3
lista_tres = [20,True]
print(lista_tres)

## Incrementa(agrega) nuevos valores
lista_tres += [32,1]
print(lista_tres)


## Listas anidadas ########################################
lista_cuatro=[1,2,3,4,["Juan","Carlos"]]
print(lista_cuatro)
print(lista_cuatro[0],)

## Imprimiendo elementos de lista anidada
print(lista_cuatro[4][0])

dato = lista_cuatro[4][1]
print(dato)

lista_prueba=[True,2,3.1416,[2055,"Carlos","Rivera"],8,"Hola"]
print(lista_prueba[3][0])
print(lista_prueba[3][1])
print(lista_prueba[3][2])



















