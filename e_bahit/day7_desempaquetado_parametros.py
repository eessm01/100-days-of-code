#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Al invocar una función, se le pueden pasar los parámetros que espera dentro de 
una lista o de un diccionario (donde los nombres de las claves equivalen al 
nombre de los argumentos). A este procedimiento se le concoce como 
desempaquetado de parámetros
"""

def imprime_argumentos(*argumentos):
    for a in argumentos:
        print(a)


# Desempaquetado de listas
parametros_lista = [1, 2, 3]
imprime_argumentos(*parametros_lista)

parametros_tupla = (5, 6, 7)
imprime_argumentos(*parametros_tupla)


# Desempaquetado de diccionarios
def imprime_argumentos_clave(**argumentos):
    for a in argumentos:
        print(argumentos[a])


parametros1 = dict(uno=1, dos=2, tres=3)
imprime_argumentos_clave(**parametros1)

parametros2 = {'cuatro': 4, 'cinco': 5, 'seis': 6}
imprime_argumentos_clave(**parametros2)

# otro ejemplo
def fun(a, b, c, d):
    print('fun')
    print(a, b)
    print(c, d)


my_list = [1, 2, 3, 4]
fun(*my_list)
