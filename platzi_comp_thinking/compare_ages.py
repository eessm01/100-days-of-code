"""Obtiene los datos de dos personas y compara las edades.

Reto de la clase 'Programas Ramíficados'
"""
def get_name():
    name = input('Ingresa tu nombre: ')
    if name:
        return name
    else: 
        print('Información inválida')
        return get_name()


def get_age():
    try:
        return int(input('Ingresa tu edad: '))
    except:
        print('Información inválida')
        return get_age()


def run():
    # usuario 1
    print('Datos del Usuario 1')
    name1 = get_name()
    age1 = get_age()
    # usuario 2
    print('Datos del Usuario 2')
    name2 = get_name()
    age2 = get_age()

    print('* ' * 20)
    print('{} tiene {} años'.format(name1, age1))
    print('{} tiene {} años'.format(name2, age2))

    if age1 > age2:
        print('{} es mayor que {}'.format(name1,name2))
    elif age1 < age2:
        print('{} es mayor que {}'.format(name2,name1))
    else:
        print('{} y {} son de la misma edad'.format(name1,name2))

    
if __name__ == '__main__':
    run()