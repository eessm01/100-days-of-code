#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Haga un script en el que se pida al usuario que indique su nombre. Evalúe si el
usuario ha dejado el campo vacío, si lo ha dejado vacío, arroje el mensaje de
error. Si no, imprima un saludo en la pantalla
"""

name = raw_input('Nombre: ')

if name:
    print('Hola, ' + name)
else:
    print('No ingreso ningún nombre')

