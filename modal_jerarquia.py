# -*- coding: utf-8 -*-
"""
*** Modal de 2 números y jerarquía aritmética ***
Created on Thu Jun 22 21:34:08 2023
@author: searchman
"""

## Modal de 2 números solicitados
num1=float( input("Ingresa el 1° número:\n") )
num2=float( input("Ingresa el 2° número:\n") )

## Obtenemos el residuo (modal) con el operador módulo '%'
modal= num1%num2
print("El residuo es: ", modal)

#Doble diagonal: // cambia a enteros
x=4
z=2
print("\nDivisión de 2 números:")
print(z,"/",x,"=",z/x)

print("\nDivisión de 2 números (redondeando a enteros):")
print(z,"//",x,"=",z//x)

## Jerarquías aritméticas
a = ( (5-3)**4)**5 + 35%3 + 255 
print("\na = ( (5-3)**4)**5 + 35%3 + 255 ")
print("a = ",a)

b = (125%3)**2 != ((8-15)**3 + 17%2)**2 +7-2%2
print("\nb = (125%3)**2 != ((8-15)**3 + 17%2)**2 +7-2%2")
print("b = ",b)
