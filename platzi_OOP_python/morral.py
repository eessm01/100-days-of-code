iterador = 0

def morral(tamano_morral, pesos, valores, n):
    """Obtiene el valor máximo de los elementos que puedo meter a un morral"""
    global iterador

    iterador += 1
    print(f'entrando a morral iteración {iterador} con n = {n}')
    # caso base:
    # ya no hay elementos o se lleno el morral
    if n == 0 or tamano_morral == 0:
        return 0

    # cuando el elemento que quiero meter al morral pesa más 
    # de lo que me queda del morral
    if pesos[n -1] > tamano_morral:
        # print(f'{pesos[n -1]} no cabe')
        return morral(tamano_morral, pesos, valores, n - 1) 

    maximo =  max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))

    # print(f'maximo valor obtenido: {maximo}')

    return maximo



if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 60
    n = len(valores)

    # valor máximo de las mezclas de los valores
    resultado = morral(tamano_morral, pesos, valores, n)

    print(resultado)