from time import time

import sys

sys.setrecursionlimit(100000000)

def factorial(n):
    factorial = 1
    
    while n > 1:
        factorial *= n
        n -= 1
    
    return factorial


def factorial_r(n):

    if n == 1:
        return 1
    
    else:
        return n * factorial_r(n - 1)



if __name__ == "__main__":
    n = 300000

    inicio = time()
    factorial(n)
    final = time()
    print(final - inicio)

    inicio = time()
    factorial_r(n)
    final = time()
    print(final - inicio)
