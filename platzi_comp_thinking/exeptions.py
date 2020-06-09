def divide_elementos(lista, divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = 0

# print(divide_elementos(lista, divisor))


def busca_pais(paises, pais):
    """
    Pais es un diccionario, pais es la llave
    Código con el principio EAFP
    (easier to ask for forgiveness than permission)
    """
    try:
        return paises[pais]
    except KeyError:
        return None

    
# las cantidades son un ejemplo    
paises_infecciones_covid19 = {
    'Brazil': 672846,
    'Colombia': 36759,
    'Mexico': 113619	
}


pais = 'Chile'
cantidad = busca_pais(paises_infecciones_covid19, pais)
if cantidad:
    print(cantidad)
else: 
    print(f'No se tiene información para {pais}')