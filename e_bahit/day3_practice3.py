#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from datetime import date

""" Crear un script en el que se le soliciten al usuario su nombre,
apellidos, y año de nacimiento. Calcular la edad del usuario en 
base a su año de nacimiento. Mostrarle un mensaje en pantalla
que muestre todos los datos aportados por el usuario más la edad
calculada
"""


first_name = str(raw_input('nombre: '))
last_name = str(raw_input('apellido: '))
year_of_birth = int(raw_input('año de nacimiento: '))

old = date.today().year - year_of_birth

print(first_name)
print(last_name)
print(year_of_birth)
print(old)
