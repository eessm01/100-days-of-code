"""Ciencia de datos con Python 2da. edición.

Manipulacion de tuplas y listas. Métodos de búsqueda.
"""

# contar cantidad de apariciones de elementos
nombres_masculinos = ["Alvaro", "Miguel", "Edgardo", "David", "Miguel"]
resultado = nombres_masculinos.count('Miguel')
print(resultado)

# obtener número de índice
# index(elemento[, indice_inicio, indice_fin])
index = nombres_masculinos.index('Miguel')
print(index)

index = nombres_masculinos.index('Miguel', 2, 5)
print(index)