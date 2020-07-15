"""Ciencia de datos con Python 2da. edición.

Manipulacion de tuplas y listas. Métodos de agregado.
"""

# agregar un elemento al final de la lista
nombres_masculinos = ['Alvaro', 'Jacinto', 'Miguel', 'Edgardo', 'David']
nombres_masculinos.append('Jose')
print(nombres_masculinos)

# Agregar varios elementos al final de la lista
otros_nombres = ['Pablo', 'Pedro']
nombres_masculinos.extend(otros_nombres)
print(nombres_masculinos)

nombres_masculinos.extend(['Julian', 'Mario', 'Alex'])
print(nombres_masculinos)

# agregar un elemento en una posición determinada
nombres_masculinos.insert(2,'Ricky')
print(nombres_masculinos)

# métodos de eliminación
# pop() retorna el elemento eliminado
r = nombres_masculinos.pop()
print(r)
print(nombres_masculinos)

# eliminar un elemento por su índice.
# retorna el elemento eliminado
r = nombres_masculinos.pop(3)
print(r)
print(nombres_masculinos)

# eliminar un elemento por su valor
nombres_masculinos.remove('Jose')
print(nombres_masculinos)

