def fibonacci(n):
    """Calcula la serie de fibonacci para n

    n int > 0
    returns int
    """
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input('Ingresa un entero: '))
result = fibonacci(n)
print(result)