# -*- coding: utf-8 -*-
"""
## Diccionarios
Created on Thu Jun 29 12:45:06 2023
@author: PILARES
"""
## Declarando diccionario 'usuario'
usuario = {
    'id_usuario': 1,
    'Nombre':'Armando',
    'Apellido':'Jiménez',
    'Carrera':'nini'
    }

print(usuario)
print(usuario['id_usuario'])
print(usuario['Carrera'])

## Método get()
print(usuario.get('Nombre'))
print(usuario.get('Apellido'))

## Cambiando valores:
print(usuario.get('Carrera'))
print(usuario['id_usuario'])
usuario['Carrera'] = 'Robótica'
usuario['id_usuario'] = 5
print(usuario.get('Carrera'))
print(usuario['id_usuario'])
