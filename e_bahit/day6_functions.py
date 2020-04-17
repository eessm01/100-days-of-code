#!/usr/bin/env python2
#-*- coding: utf-8 -*-

""" Una funcion es una forma de agrupar expresiones y algoritmos
de forma tal que queden contenidos dentro de 'una cápsula', que
solo pueda ejecutarse al ser invocada. Una vez que es definida,
puede ser invocada tantas veces como sea necesario.
A las funciones provistas por el lenguaje se les denomida 
'Built-in functions'

def funcion():
    # algoritmo identado

- se ejecuta solo cuando es invocada
- puede regresar datos
- puede recibir parámetros que son de ámbito local y se le deben pasar
  en el mismo orden en el que se espera
- existen parámetros por omisión que son definidos después de los 
  obligatorios
- Python permite llamar a una función pasándole los argumentos esperados
  como pares de clave=valor
"""

def mi_funcion():
    print("Hola, mundo!")


mi_funcion()  # en este momento se ejecuta mi_funcion


def funcion():
    return "Hola, mundo!"


frase = funcion()
print(frase)


funcion()  #aquí se ejecuta la función, pero se ignora el resultado


def mi_funcion_params(param1, param2):
    print(param1)
    print(param2)


mi_funcion_params('Ey, está es una función', 'con parámetros')


def calcular_neto(bruto, alicuota=21):
    iva = bruto * float(alicuota) / 100
    neto = bruto + iva
    return neto


neto1 = calcular_neto(100)
print(neto1)

neto2 = calcular_neto(100, 10.5)
print(neto2)


