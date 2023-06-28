# -*- coding: utf-8 -*-
"""
## Ejercicio:
    Se quiere realizar un programa que lea por teclado
    las 9 notas obtenidas por un alumno comprendidas
    entre (0 - 10). A continuación debe mostrar todas
    las notas, la nota media, la nota más alta, y la
    nota menor.
    
Created on Wed Jun 28 12:25:10 2023
@author: PILARES
"""

notas = []

for i in range(0,9):
    # condicional tomando como ref. rango: 0-10
    while True:
        nota = float(input("Ingresa tu nota %d:"%i))
        
        if nota>=0 and nota<=10:break;
            #break=rompe ciclo de bucle y regresa
    notas.append(nota)

print(notas)
        
        
            
        


