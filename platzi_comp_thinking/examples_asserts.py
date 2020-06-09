# assert <expression_boolean>, <mensaje_de_error>

def primeras_letras(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es string'
        assert len(palabra) > 0, 'No se permiten valores vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras


lista_de_palabras = ['erase','','ve','un gato']

lista_de_letras = primeras_letras(lista_de_palabras)

for letra in lista_de_letras:
    print(letra)