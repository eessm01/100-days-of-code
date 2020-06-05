estudiantes = {
    'mexico': 10,
    'colombia': 15,
    'puerto_rico': 4
}

# forma de iterar sobre las keys del diccionario
for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
    print(pais)

# forma de iterar sobre los valores del diccionario
for numero_de_estudiantes in estudiantes.values():
    print(numero_de_estudiantes)

# forma de iterar sobre keys y valores al mismo tiempo
for pais, numero_de_estudiantes in estudiantes.items():
    print(f'{pais} : {numero_de_estudiantes}')

for pais in estudiantes:
    print(f'{pais} : {estudiantes[pais]}')


