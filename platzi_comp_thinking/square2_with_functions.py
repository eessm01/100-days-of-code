"""Obtiene la raiz cuadrada de un número

Por medio de un menú de opciones puede seleccionarse
el método para calcular la raiz cuadrada de un número
"""

def get_number():
    """Obtiene un string desde la consola
    
    returns int
    """
    try:
        return int(input('Ingresa un número: '))
    except:
        return get_number()


def run_enumeration(object_):
    """Método de enumeración exahustiva para calcular la raiz cuadrada

    object_ int número objetivo para calcular su raiz cuadrada
    returns result float, tal que result**2 = object_
    """
    result = 0

    while result**2 < object_:
        result += 1

    if result**2 == object_:
        return result
    else:
        return None


def run_approximation(object_, epsilon):
    """Método de aproximación para calcular la raiz cuadrada
    
    object_ int número del que se calculará la raiz cuadrada
    epsilon float precisión para el calculo
    returns result float raiz cuadrada de object_
    """
    step = epsilon**2
    result = 0.0
    new_epsilon = object_
    iterations = 0

    while new_epsilon >= epsilon:
        result += step
        iterations += 1
        new_epsilon = object_ - result**2

    return result


def run_binary_search(object_, epsilon):
    """Método de búsqueda binaria para calcular la raiz cuadrada

    object_ int número del que se calculará la raiz cuadrada
    epsilon float precisión para el calculo
    returns result float raiz cuadrada de object_
    """
    epsilon = 0.0001
    min_ = 0.0
    max_ = max(1.0, object_)  #regresa el mayor de esos dos valores
    result = (min_ + max_) / 2
    iterations = 0

    while abs(object_ - result**2) >= epsilon:
        if result**2 < object_:
            min_ = result
        else:
            max_ = result

        result = (min_ + max_) / 2
        iterations += 1

    return result


if __name__ == "__main__":
    epsilon = 0.001
    object_ = 0
    result = 0

    while True:
        print("* * Menú de opciones * *\n \
        [E]numeración exahustiva\n \
        [A]proximación\n \
        [B]úsqueda binaria\n \
        [S]alir \n")

        option = input('Ingresa una opción: ').upper()

        if option == 'S':
            break
        elif option == 'E':
            object_ = get_number()
            result = run_enumeration(object_)
        elif option == 'A':
            object_ = get_number()
            result = run_approximation(object_, epsilon)
        elif option == 'B':
            object_ = get_number()
            result = run_binary_search(object_, epsilon)
        else:
            print('Opción inválida')

        if result:
            print(f'La raiz cuadrada de {object_} es {result}')
        else:
            print(f'No se encontró la raiz cuadrada de {object_}')