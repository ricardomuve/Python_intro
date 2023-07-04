# -*- coding: utf-8 -*-
"""
## Ejercicio: 
    - Inicializar lista vacia
    - Llenarla con 20 valores aleatorios
        (usando Random)
    - Mostrar el valor elevado al cuadrado y al cubo

Created on Tue Jul  4 11:12:15 2023
@author: PILARES
"""

## Paquetería para generar números aleatorios
import random
## Declaramos lista vacía
lista = []
## Bucle 
for i in range(0,20):
    # Número entero aleatorio entre 1-30
    num = (random.randint(1, 30))
    # Agregamos valor a la lista
    lista.append(num)
      

for numero in lista:
    print("\nNúmero aleatorio: ",numero)
    print("Su cuadrado es: ", numero**2)
    print("Su cubo es: ", numero**3)
    