#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Funciones con parámetros por omisión, permite que la función sea llamada
con menos argumentos de los que se definió.
- La definición debe anteceder los líneas en blanco.
- Al asignarse parámetros por omisión, no deben dejarse espacios ni antes
ni después del signo =
- Los parametros por omisión deben ser definidos a continuación de los
  parámetros obligatprios.

Keyword arguments, son una característica de Python, permite llamar a una
función pasándole los argumentos esperados como pares de clave=valor

Parámetros arbitrarios, es posible que una función espere recibir un número
arbitrario (desconocido) de argumentos. Estos argumentos llegaran a la
función en forma de tupla.
Para definir argumentos arbitrarios en una función, se antecede un asterisco
(*) al nombre del parámetro
Los parámetros arbitrarios siempre deben suceder a los obligatorios
Es posible también obtener parámetros arbitrarios como pares de clave=valor.
En estos casos, al nombre del parámetro deben precederle dos asteriscos(**)

El recorrido de los parámetros arbitrarios es como el recorrido de 
cualquier tupla (para parámetros arbitrarios sin clave) o de cualquier
diccionario, para parámetros arbitrarios con clave
"""

def calcular_neto(bruto, alicuota=21):
    iva = bruto * float(alicuota) / 100
    neto = bruto + iva
    return neto


def funcion_keyword_arg(obligatorio1, opcional1='opcional1', opcional2=15):
    print(obligatorio1)
    print(opcional1)
    print(opcional2)


def funcion_arbitrarios(obligatorio, *arbitrarios):
    pass


def funcion_recorre_arbitrarios(obligatorio, *arbitrarios):
    print(obligatorio)
    
    for argumento in arbitrarios:
        print(argumento)


def recorre_arbitrarios_clave(obligatorio, **arbitrarios):
    print(obligatorio)
    for argumento in arbitrarios:
        print(arbitrarios[argumento])


neto1 = calcular_neto(100)

neto2 = calcular_neto(100, 10.5)

funcion_keyword_arg('valor obligatorio', opcional2=1234)

funcion_arbitrarios('fijo')
funcion_arbitrarios('fijo', 1)
funcion_arbitrarios('fijo', 1, 2, 3)

funcion_recorre_arbitrarios('solo un parámetro')
funcion_recorre_arbitrarios('hola', 1, 2, 3, 4, 5)

funcion_recorre_arbitrarios('fiu')
funcion_recorre_arbitrarios('fiu', 'lala')
funcion_recorre_arbitrarios('fiuu',1, 2, 4, 5, 6, 7, 8, 9)

recorre_arbitrarios_clave('arbitrarios clave')
recorre_arbitrarios_clave('arbitrarios clave', uno=1, dos=2, tres=3, cuatro=4)

