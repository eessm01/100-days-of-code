from random import randint



def busqueda_binaria(lista, comienzo, final, objetivo, contador):
    contador += 1
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    # caso base
    if comienzo > final:
        print(f'numero de iteraciones: {contador}')
        return False

    medio = (comienzo + final) // 2  # sin tomar en cuenta los decimales 

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo, contador)


if __name__ == "__main__":
    contador = 0
    tamano_lista = int(input('¿De que tamano sera la lista? '))
    objetivo = int(input('¿Que numero quieres encontrar? '))

    lista = sorted([randint(0, tamano_lista) for i in range(tamano_lista)])  # ordena la lista

    print(lista)

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo, contador)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') 