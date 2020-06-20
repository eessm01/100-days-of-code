# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Perro:

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        """Get del método nombre"""
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo):
        print('Modificando nombre..')
        self.__nombre = nuevo
        print('El nombre se ha modificado por')
        print(self.__nombre)

    @nombre.deleter
    def nombre(self):
        print('Borrando nombre.. ')
        del self.__nombre
    

if __name__ == "__main__":
    tomas = Perro('Tom')
    print(tomas.nombre)

    tomas.nombre = 'Tomasito'
