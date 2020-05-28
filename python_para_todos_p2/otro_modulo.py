CONSTANTE = 3

def una_funcion():
    print("una función (otro_modulo)")


def otra_funcion():
    print("otra funcion 2 (otro_modulo)")


class UnaClase:
    def __init__(self):
        print("Una clase (otro_modulo)")
    

print("un modulo y se muestra siempre (otro_modulo)")

if __name__ == '__main__':
    print("Se muestra si no es importación (otro_modulo)")


