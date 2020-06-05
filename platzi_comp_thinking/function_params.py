def nombre_completo( nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

string = nombre_completo('David', 'Aroesti')
print(string)
string = nombre_completo('David', 'Aroesti', inverso=True)
print(string)
string = nombre_completo(inverso=True, apellido='Aroesti', nombre='David')
print(string)
