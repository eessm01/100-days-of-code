from random import randint

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == "__main__":
    tamano_lista = int(input('¿De que tamano sera la lista? '))
    objetivo = int(input('¿Que numero quieres encontrar? '))

    lista = [randint(0, 100) for i in range(tamano_lista)]

    print(lista)
    encontrado = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') 