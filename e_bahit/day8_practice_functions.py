#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from datetime import date

"""
Una función puede llamar a otra función que retorno un valor. Esto se conoce 
como llamada de retorno. 
La llamada interna a otra función puede almacenarse, retornarse o ignorarse.
Cuando la llamada que se hace es a la misma función que se llama, se conoce
como LLAMADA RECURSIVA.

Un función puede tener cualquier tipo de algoritmo y cualquier cantidad de
instrucciones. Sin embargo, una buena práctica indica que la finalidad de una
fución, debe ser REALIZAR UNA ÚNICA ACCIÓN.
"""


def get_edad(birth_year):
    current_year = date.today().year    
    old = current_year - birth_year
    return old


def get_birth_year():
    birth_year = raw_input("Año de nacimiento: ")
    
    if not birth_year:
        birth_year = get_birth_year()

    return birth_year


def get_name():
    name = raw_input("nombre: ")
    
    if not name:
        name = "NN"

    return name


def run():

    birth_year = int(get_birth_year())
    old = get_edad(birth_year)

    name = get_name()

    print(old)
    print(name)


if __name__ == "__main__":
    run()

