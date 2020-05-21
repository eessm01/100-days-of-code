#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from libs.mod_edad import get_edad

anio_nac = int(input('Año de nacimiento: '))
edad = get_edad(anio_nac)
quedan = 100 - edad
print('wooo, te quedan {anios} para cumplir 100'.format(anios=quedan))


