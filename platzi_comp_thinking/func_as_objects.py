"""Ejemplos de funciones como un objeto
"""

# Argumentos de otras funciones
def multiplicar_por_dos(n):
    return n * 2


def sumar_dos(n):
    return n + 2


def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados


nums = [1, 2, 3]
nums1 = aplicar_operacion(multiplicar_por_dos, nums)
print(nums1)
nums2 = aplicar_operacion(sumar_dos, nums)
print(nums2)


# Funciones en expresiones
sumar = lambda x, y: x + y
print(sumar(2,3))


# Funciones en estructuras de datos
def aplicar_otra_operacion(num):
    operaciones = [abs, float]
    
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    
    return resultado


resultado = aplicar_otra_operacion(-2)
print(resultado)