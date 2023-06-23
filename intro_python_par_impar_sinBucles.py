# -*- coding: utf-8 -*-
"""
*** Número par/impar (Sin bucles) ***
Created on Thu Jun 22 21:29:06 2023
@author: searchman
"""

######## Método1 #####################################################

print("\n>> Programa que detecta si un número es par/impar <<")
numero=int(input("Ingresa un número: "))
par= numero%2
print("\t Indicador: ",par)
print("Indicador = 0 : Número par")
print("Indicador = 1 : Número impar")

######## Método2 #####################################################

print("\n>> Programa que detecta si un número es par/impar <<")
numero=int(input("Ingresa un número: "))
par= numero%2
print("¿Número par?:", par==0)

######## Método3 #####################################################

print("\n>> Programa que detecta si un número es par/impar <<")
numero=int(input("Ingresa un número: "))
par= (numero%2) != 0
print("¿El número ", numero, " es impar?", par)
