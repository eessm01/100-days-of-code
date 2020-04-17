#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" 
1. Definir una lista que contenga los 10 primeros nùmeros de la serie de
Fibonacci.
2. Definir una lista cuyos elementos sean 4 tuplas, con dos valores cada una:
nombre, y año de nacimiento.
3. Utilizar los elementos de la lista del punto 2 para generar un diccionario
en el que las claves sean los nombres de la lista del punto 2, y como valor
asociado, la edad calculada en base al año asignado como segundo valor de la
tupla de cada elemento de la lista.
"""

fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

people_list = [('Sergio', 1981),
                ('Carmen', 1980),
                ('Gibran', 2013),
                ('Julio', 2018)]

people_dic = {}

for elemento in people_list:
    people_dic[elemento[0]] = 2020 - elemento[1]

print(fibonacci_list)
print(people_list)
print(people_dic)
