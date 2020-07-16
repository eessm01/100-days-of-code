"""Ciencia de datos con Python 2da. edición.

Concatenación de colecciones.
"""

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6, 7, 9]
lista3 = lista1 + lista2
print(lista3)

tupla1 = (1, 2, 3, 4, 5)
tupla2 = (4, 6, 8, 10)
tupla3 = (3, 5, 7, 9)
tupla4 = tupla1 + tupla2 + tupla3
print(tupla4)

# valor maximo
print(max(tupla4))
print(max(tupla3))

# contar elementos
print(len(lista3))
print(len(lista2))