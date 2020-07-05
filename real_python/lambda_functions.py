"""Real Python. How to Use Python Lambda Functions

Lambda function are frecuently used with higher-order functions, 
wich take one or more funcions as argument or return one or 
more funcions.

Python exposes higher-order functions as built-in functions
or in the standar library. Examples include map(), filter(), 
functools.reduce(), as well as key functions like sort(), 
sorted(), min(), max()
"""

print((lambda x: x + 1)(20))

add_one = lambda x: x + 1
print(add_one(3))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

hig_orf_func = lambda x, func: x + func(x)
result = hig_orf_func(2, lambda x: x*x)
print(result)
result = hig_orf_func(5, lambda x: x*x)
print(result)


print(
    (lambda x: (x % 2 and 'odd' or 'even'))(3)
)

def full_name(first: str, last: str) -> str:
    return f'{first.title()} {last.title()}'

print(full_name('carmen', 'sanchez'))

r = (lambda x, y, z: x + y + z)(1, 2, 3)
print(f'r: {r}')

r = (lambda x, y, z=3: x + y + z)(1, 2)
print(f'r: {r}')

r = (lambda x, y, z=3: x + y + z)(1, y=2)
print(f'r: {r}')

r = (lambda *args: sum(args))(1, 2, 3)
print(f'r: {r}')

r = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
print(f'r: {r}')

r = (lambda x, *, y, z: x + y + z)(1, y=2, z=3)
print(f'r: {r}')


def some_decorator(f):
    def wraps(*args):
        print(f'Calling funtion {f.__name__}')
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f'With argument {x}')


decorated_function(5, 7, '22', {'uno':1})

decorated_function(6)

# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f'[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}')
        return f(*args, **kwargs)
    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
print( 
    add_two(x=5) 
)

def add_five(x):
    return x + 5

print(
    trace(add_five)(7)
)

# Applying decorator to a lambda
print(
    (trace(lambda x: x ** 2))(3)
)

lista = list(map(trace(lambda x: x ** 2), range(5)))
print(lista)


# closures
def outer_func(x):
    y = 4
    def inner_func(z):
        print(f'x = {x}, y = {y}, z = {z}')
        return x + y + z
    return inner_func


for i in range(3):
    closure = outer_func(i)
    print(f'closure({i+5}) = {closure(i+5)}')


def outer_func_lambda(x):
    y = 4
    return lambda z: x + y + z

print()

for i in range(3):
    closure = outer_func_lambda(i)
    print(f'closure({i+5}) = {closure(i+5)}')


print('* * * Evaluation Time * * * ')

def wrap(n):
    def f():
        print(n)
    return f

numbers = 'one', 'two', 'three'  # this is a tuple
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()

print('Whit lambda funcion')

funcs2 = []
for n in numbers:
    funcs2.append(lambda: print(n))

for f in funcs2:
    f()

print('Whit lambda funcion, assign the free variable at definition time')

funcs2.clear()

for n in numbers:
    funcs2.append(lambda x=n: print(x))

for f in funcs2:
    f()