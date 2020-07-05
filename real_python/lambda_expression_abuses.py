"""Real Python. How to Use Python Lambda Functions

If written in the context of professional Python code, 
would qualify as abuses.

There are a fews examples of lambda usages that should be avoided.

* It doesn't follow the Python styles (PEP 8)
* It's cumbersome and difficult to read
* It's unnecesarily clever at the cost of difficult readability
"""

# You can but should not write class methods as Python lambda functions.
class Car:
    """Car with methods as lambda functions."""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    brand = property(lambda self: getattr(self, '_brand'),
                     lambda self, value: setattr(self, '_brand', value)
    )

    # better implementation for brand
    # @property
    # def brand(self):
    #     return self._brand

    # @brand.setter
    # def brand(self, value):
    #     self._brand = value


    year = property(lambda self: getattr(self, '_year'),
                    lambda self, value: setattr(self, '_year', value)
    )

    __str__ = lambda self: f'{self.brand} {self.year}'  #1: error E731

    # better implmentation
    # def __str__(self):
    #     return f'{self.brand} {self.year}'

    honk = lambda self: print('Honk!') # 2: error E731


car = Car('bb', 2013)

# You'll learn to replace map() and lambda with list comprehensions or generator expressions.
# (lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10])
another_list = (lambda some_list: list(map(lambda n: n // 2, some_list)))([1,2,3,4,5,6,7,8,9,10])
print(another_list)

def throw(ex): raise ex
(lambda: throw(Exception('Something bad happened')))()