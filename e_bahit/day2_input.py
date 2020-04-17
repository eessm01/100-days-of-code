#!/usr/bin/env python2
from datetime import date

""" Day 2. Script que pida un dato al usuario y muestre en pantalla """

burn_year = int(raw_input("What's is your burn year? :"))

current_year = date.today().year

old = current_year - burn_year

print(old) 


