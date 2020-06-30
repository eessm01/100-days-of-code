#!/usr/bin/env python2
#-*- coding:utf-8 -*-
"""The Original Hacker N.4. Wrappers y Decoradores.

- Un CLOSURE una fución que dentro de ella define
otra función y la devuelve cuando se le invoca.
- Un DECORATOR es un closure que recibe una función
como parámetro.
- Una FUNCION DECORADA es la que se para como parámetro
a un decorador.
- Un WRAPPER es la función interna del decorador,
encargada de retomar la función decorada.

Orden de ejecución en wrappers y decoradores:
1. decorador (automáticamente al ejecutar el script
remplazando la función decorada por el wrapper)
2. wrapper (al invocar a la función decorada)
3. función decorada (luego de ejecutarse el wrapper)

Puede decirse entonces que conceptualmente, un 
decorador es un closure que se encarga de remplazar
a la función decorada por su función interna, a la 
cuál se le denomina wrapper
"""

def decorador(funcion):
    print('Soy el decorador()')

    def wrapper():
        print('Soy el wrapper()')
        return funcion()
    
    return wrapper


@decorador
def funcion_decorada():
    print('Soy la funcion_decorada()')


funcion_decorada()