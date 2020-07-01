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