#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from datetime import date

""" Crear un script en el que se le soliciten al usuario su nombre,
apellidos, y año de nacimiento. Calcular la edad del usuario en 
base a su año de nacimiento. Mostrarle un mensaje en pantalla
que muestre todos los datos aportados por el usuario más la edad
calculada.

Agregar una validación de entrada
Si el usuario deja el nombre en blanco (if nombre ==""), defina nombre
por defecto con el valor "NN".
Si deja el apellido en blanco, volver a pedir el apellido.
Hacer que todo lo que imprime el script, sólo se imprima si el año
de nacimiento es menor que 2005. En caso contrario, muestre el mensaje
"Necesitas permisos de tus padres para ver el resultado"
"""


first_name = str(raw_input('nombre: '))
last_name = str(raw_input('apellido: '))
year_of_birth = int(raw_input('año de nacimiento: '))


def print_information(pfirst_name, plast_name, pyear_of_birth):
   
    if pfirst_name == "":
        pfirst_name = "NN"
 
    while not plast_name:
        plast_name = str(raw_input('apellido: '))

    old = date.today().year - pyear_of_birth

    if pyear_of_birth > 2005:
        print("Necesitas permiso de tus padres para ver los resultados")
    else:
        print(pfirst_name)
        print(plast_name)
        print(pyear_of_birth)
        print(old)


print_information(first_name, last_name, year_of_birth)
