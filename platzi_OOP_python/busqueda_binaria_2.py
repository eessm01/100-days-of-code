from random import randint


def busqueda_binaria(lista, objetivo):
    print(lista)

    if len(lista) == 0:
        return False
    
    mitad = len(lista) // 2

    # caso base
    if objetivo == lista[mitad]:
        return True

    # recursividad
    elif objetivo < lista[mitad]:
        return busqueda_binaria(lista[0:mitad], objetivo)
    elif objetivo > lista[mitad]:
        return busqueda_binaria(lista[mitad+1:len(lista)], objetivo)


if __name__ == "__main__":

    objetivo = int(input('Ingresa un número: '))
    lista = sorted([randint(1,100) for i in range(0,21) ])

    print('Lista generada')
    print(lista)
    78
    encontrado = busqueda_binaria(lista, objetivo)

    print(f'número {objetivo} {"encontrado" if encontrado else "no encontrado"}')