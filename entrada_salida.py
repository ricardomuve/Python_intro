# -*- coding: utf-8 -*-
"""
*** Entrada y sailda de datos ***
Created on Thu Jun 22 21:10:43 2023
@author: searchman
"""

## Declaración y asignación de variable (int)
numero_fijo = 100

## Imprimios el valor de la variable 
print("Asignación interna: ")
print("Número1 = ", numero_fijo)


#Convertimos un string a entero con el método 'int()'
nota=int( input("\nIngresa un número entero: ") )
print("Asignación por ingreso de datos: ")
print("Número2 = ", nota)

## Declaración y asignación de variable (string)
nombre="Juan"

## Transformamos un entero a string con el método 'str()'
nota_str=str(nota)

#Se imprime sumando los 2 strings
print("\nStrings sumados:")
print(nota_str + nombre)

#Convertimos a real(float) un dato con el método 'float()'
promedio=float(input("\nIngresa un número real: "))
print("Número ingresado: ",promedio)


""" Ejercicio: Solicitar 5 calificaciones 
        y calcular el promedio.    
"""
nomb=input("\nIngresa tu nombre: ")
nota1=float(input("Ingresa tu nota N°.1: "))
nota2=float(input("Ingresa tu nota N°.2: "))
nota3=float(input("Ingresa tu nota N°.3: "))
nota4=float(input("Ingresa tu nota N°.4: "))
nota5=float(input("Ingresa tu nota N°.5: "))

prom=(nota1+nota2+nota3+nota4+nota5)/5
print("Estudiante: \n",nomb)
print("Promedio final: \n",prom)

## aumentar +10 al imprimir un entero
numero = int( input("Ingresa el número:") )
print(numero+10)

## Imprimir 5 veces una variable
var=input("Ingresa una palabra: ")
var*=5
print(var)


