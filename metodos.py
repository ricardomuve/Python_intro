# -*- coding: utf-8 -*-
"""
## Métodos
Created on Wed Jun 28 11:28:36 2023
@author: PILARES
"""
# Nueva lista
lista = ["José","Arturo"]
print(lista)
print(lista)
print(lista[-1])
print(lista[1:])
print(lista[:2])

# Método append=agrega elementos al final de la lista
print("\nMétodo 'append'")
print(lista)
lista.append("Carlos")
print(lista)


print("\nMétodo 'extend'")
# Método extend=agrega elementos al final de la lista
lista_dos=[1,2,3,4]
print(lista_dos)
lista_dos.extend([5])
print(lista_dos)
lista_dos.extend(['hola'])
print(lista_dos)

nums=(33,44,55,44,44)
# Método extend con variable como argumentos
lista_dos.extend(nums)
print(lista_dos)

# Método index devuelve el indice donde el argumento aparece por 1° vez
print("\nMétodo 'index() arg=44'")
print(lista_dos)
m_index = lista_dos.index(44)
print("Index donde aparece por 1° vez el 44= ", m_index)


# Método reverse invierte las posiciones de la lista
lista_dos.reverse()
print(lista_dos)

# Método sort: ordena de manera ascendente la lista (¡mismo tipo de dato!)
print("\nMétodo 'sort'")
lista_tres = [1,-1,10,5]
print(lista_tres)
lista_tres.sort()
print(lista_tres)


listest = [False,True,False,True,True,False]
print(listest)
listest.sort()
print(listest)

listest2 = ['z','Z','A','a']
print(listest2)
listest2.sort()
print(listest2)

# Método clear (vacía la lista)
print("\nMétodo 'clear'")
print(lista_dos)
lista_dos.clear()
print(lista_dos)

# Método copy ()
print("\nMétodo 'copy'")
lista_nueva=[22,23,24]
#Copiamos todo de lista_dos a lista_nueva_copy
lista_nueva_copy = lista_nueva.copy()
# agregamos un elemento
lista_nueva.append(100)

print("a=",lista_nueva,"\nb=",lista_nueva_copy)


## Método count (cuenta las veces que aparece un argumento)
print("\nMétodo 'count'")
lista_contar = [1,1,1,2,3,3,4,4]
cont = lista_contar.count(1)
print("lista_contar:",lista_contar)
print("lista_contar.count(1)=",cont)

























