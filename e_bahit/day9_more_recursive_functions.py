#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Defina dos funciones ("a" y "b")
Haga que "a" llame a "b"
Haga que "b" se llame a sí misma.
No se asuste si algo sale mal y la shell parece descontrolarse
Si sucede, pulse Crtl + C o Ctrl + D si la cuestión se pone dificil :D
EQUIVOCARSE o liarla, lo ayudará a entender mejor cómo funcionan las 
llamadas recursivas.
"""

def a():
    text = b() + " y esta es la función a"
    return text


def b():
    b()
    return "Esto es b" 


a = a()
print(a)





