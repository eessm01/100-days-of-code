#-*- coding: utf-8 -*-
"""
Retrocompatibilidad:
Es uno de los principios por los que un lenguaje de programación se sustenta
y Es la capacidad que el intérprete del un lenguaje de programación, posee
para interpretar programas desarrollador por una versión previa del mismo
lenguaje.

Tener dos versiones de un programa para ejecutarse una en python2 y otra 
en python3, implica el mantenimiento de ambas versiones del mismo script.
"""
from libs.retrocompatibilidad import echo, get

# imprimir un texto en la pantalla
# python2: print "Hola Mundo!"
# python3: print("Hola Mundo!")
echo("Hola Mundo!")


# Solicitar datos al usuario
# python2: raw_input("Nombre: ")
# python3: input("Nombre: ")
nombre = get("Nombre: ")
echo(nombre)
