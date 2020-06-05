"""Obtiene la raiz cuadrada de un número

Con el método de aproximación de soluciones, este programa
obtiene la raiz cuadrada de un número.
La aproximación implica un margen de error llamado epsilon,
para obtener un resultado que sea menor a ese margen de error.
"""

objetivo = int(input('Escoge un número: '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0
new_epsilon = objetivo
iteraciones = 0

while new_epsilon >= epsilon:
    # print(new_epsilon, respuesta)
    respuesta += paso
    iteraciones += 1
    new_epsilon = objetivo - respuesta**2

if new_epsilon <= epsilon:
    print(f'En {iteraciones} iteraciones y epsilon = {epsilon}, se encontró la raiz cuadrada de {objetivo} que es {respuesta}')
else:
    print(f'No se encontró la raiz cuadrada de {objetivo}')
