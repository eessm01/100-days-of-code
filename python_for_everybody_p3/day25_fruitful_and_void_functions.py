"""Fruitful functions, void functions, parameters and arguments
"""
import math

def print_twice(bruce):
    """This function assigns the argument to a parameter named bruce."""
    print(bruce)
    print(bruce)


print_twice('Spam')
print_twice(17)
print_twice(math.pi)

# The argument is evaluated before the function is called
print_twice('Spam ' * 4)
print_twice(math.cos(math.pi))

# The name of the variable we pass as an argument (michael) has nothing 
# to do with the name of the parameter (bruce)
michael = 'Eric, the half a bee.'
print_twice(michael)

# If you try to assign the result to a variable, you get a special 
# value called None. <class 'NoneType'>
result = print_twice('Bing')
print(result)


def addtwo(a, b):
    added = a + b
    return added


x = addtwo(3, 5)
print(x)