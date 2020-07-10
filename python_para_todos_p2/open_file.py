"""Python para todos. Archivos.

Abrir archivos
"""

f = open("21days_of_abundance_day4.txt")

print('Completo: ')
completo = f.read()
print(completo)

print('Una Parte: ')
f = open("21days_of_abundance_day4.txt")
parte = f.read(120)
print(parte)

print('linea por linea: ')
f = open("21days_of_abundance_day4.txt")
while True:
    linea = f.readline()
    if not linea: break
    print(linea)


print('Todas las lineas')
f = open("21days_of_abundance_day4.txt")
line_list = f.readlines()
print(len(line_list))

for linea in line_list:
    print(linea)

# Una vez terminemos de trabajar con el archivo debemos cerrarlo 
# utilizando el método close.
f.close()