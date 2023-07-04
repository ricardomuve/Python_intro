# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:10:09 2023

@author: PILARES
"""

dAlumnos={}
notas=[]

num_alumnos=int(input("Ingresa la cantidad de alumnos: "))
for i in range (num_alumnos):
    nombre=input("Ingresa nombre del alumno ")
    cal=1
    notas=[]
    while nombre in dAlumnos:
        print("Alumno ya registrado")
        nombre=input("Ingresa nombre del alumno ")
    while cal>0:
        while True:
            cal=float(input("Introduce calificación "))
            if cal>=0 and cal<=10:
                notas.append(cal)
                break
            elif cal<0:
                break
            print("Introduce una nota entre 0 y 10")


    dAlumnos[nombre]=notas[:]

print(dAlumnos) 