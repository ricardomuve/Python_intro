# -*- coding: utf-8 -*-
"""
# Solicitar valor
# Imprimir su facotiral
# Usar funciones

Created on Tue Jul 11 12:21:43 2023
@author: PILARES
"""
## Método 1 ###########################################################
#Función para ver si es entero positivo
def validar(numero):
    #
    if numero>0:
        res = factorial_uno(num)
    else:
        print("Número negativo -no válido-")
    return res
#*********************************************************************#
#Definimos función de factorial
def factorial_uno(numero):
    #Declaramos e inicializamos variable de resultado
    resul=1
    #Ciclo para calcular factorial
    while numero !=0:
        # usamos operador de asignación para multiplicar los valores
        resul *= numero
        #Decrementamos numero
        numero -=1
    # Devolvemos resultado
    
    return resul

#*********************************************************************#   

print("\tPrograma que calcula el factorial de un número.")
num = int(input("Ingresa el número: "))

# Mandamos llamar función factorial()
valor = validar(num)

print("El factorial de ",num,"es: ",valor)





## Método 2 ###########################################################
#Definimos función de factorial
def factorial(resultado=1):
    num=int(input("Ingresa el número para su factorial: "))
   
    # ciclo 
    for contador in range(num):
        resultado += (resultado*contador)
    return resultado


print("\tPrograma que calcula el factorial de un número (2).")
print("El factorial de ",num,"es: ",factorial() )






















