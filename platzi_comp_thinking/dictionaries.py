my_dict = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50
}

print(my_dict)

valor = my_dict.get('Juan', 99)
print(valor)

valor = my_dict.get('Jaime', 30)
print(valor)

my_dict['Jaime'] = 20
print(my_dict)

my_dict['Pedro'] = 42
print(my_dict)

del my_dict['Jaime']
print(my_dict)


for llave in my_dict.keys():
    print(llave)


for valor in my_dict.values():
    print(valor)


for llave, valor in my_dict.items():
    print(llave, valor)


esta = 'David' in my_dict
print(esta)

esta = 'Tom' in my_dict
print(esta)

# comprehension
other_dict = {x: x**2 for x in (2, 4, 6)}
print(other_dict)