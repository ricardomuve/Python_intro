# -*- coding: utf-8 -*-
"""
## Funciones
Created on Tue Jul 11 11:22:49 2023
@author: PILARES
"""


## Ejemplo1 ############################################
# Definimos la función 'datos' y lo que realizará
def datos(nombre,edad):
    
    print("Mi primer función")
    
    #Obtenemos valor de la variables e imprimimos
    print("Nombre: ", nombre)
    print("Edad: ", edad)


## Ejemplo2 ############################################
# Definimos la función 'suma'
# Los parámetros se pueden definir al inicio
def suma(numero=4,numero_dos=100):
    resultado=numero+numero_dos
    #Variable de retorno
    return resultado


## Ejemplo3 ############################################
# No se puede inicializar sólo un valor
def resta(numero=100, numDos):
    resultado=numero-numDos
    #Variable de retorno
    return resultado

## Ejemplo4 ############################################

def resta(numero, numDos):
    resultado=numero-numDos
    #Variable de retorno
    return resultado



## Ejemplo5 ############################################

def saludo():
    #Variable de retorno
    return ("Hola Mundo")


## Ejemplo5 ############################################

def saludo_dos():
    # Solicitamos nombre y edad
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu nombre: "))
    #Variable de retorno en forma de tupla
    return nombre,edad

## Ejemplo6 ############################################

def saludo_tres():
    # Solicitamos nombre y edad
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu nombre: "))
    #Variable de retorno un sólo string
    return nombre+str(edad)


## Ejemplo7 ############################################

def alumno(nombre,carrera="Informática"):
    # Solicitamos nombre y edad
    print("Nombre: ",nombre,"\nCarrera: ",carrera)


## Ejemplo8 ############################################

def alumno_dos(carrera="Informática"):
    # Solicitamos nombre
    nombre = input("Ingresa tu nombre: ")    
    print("Nombre: ",nombre,"\nCarrera: ",carrera)


## Ejemplo9 ############################################

def saludo():
    print("Bienvenidos a Escuela de Código")
    
def alumno(nombre,edad):
    print(nombre,edad)
    return saludo()

## Ejemplo10 ############################################
def jugar(intentos=1):
    respuesta = input("¿De qué color es el cielo?")
    while respuesta:
        respuesta = input("¿De qué color es el cielo?")
        #Validamos respuesta
        if respuesta != "azul":
            if intentos <=3:
                print("Fallaste")
                intentos += 1
            else:
                print("Game Over")
                break
        else:
            print("Ganaste!")
            
        
        
        

#******************************************************#
# Mandamos llamar la función con 2 parámetros    
datos("Rick",31)

# Llamamos función suma
suma()

# Llamamos función resta con 2 parámetros
resta(12,10)

# Llamamos función saludo
saludo()

# Llamamos función saludo_dos
print(saludo_dos())
saludo_dos()
# tipo de dato regresado por saludo_dos
type(saludo_dos())

# Llamamos función saludo_dos
print(saludo_tres())
saludo_tres()

# Llamamos función alumno
alumno("Rick")

# Llamamos función alumno_dos
alumno_dos()

#Llamamos función anidada del ejemplo 9
alumno("Rick",31)


jugar()
