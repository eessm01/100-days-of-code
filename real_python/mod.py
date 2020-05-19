"""
╰─$ python3                                                                                                                                                                                                       127 ↵
Python 3.7.7 (default, Mar 10 2020, 15:43:03) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mod
>>> print(mod.s)
If Comrade Napoleon says it, it must be right
>>> mod.a
[100, 200, 300]
>>> mod.foo(['quux', 'corge', 'grault'])
arg = ['quux', 'corge', 'grault']
>>> x = mod.Foo()
>>> x
<mod.Foo object at 0x102bfc210>
>>> 

sys.path.append(r'/Users/car/100daysofcode/real_python')
>>> sys.path

>>> import mod
>>> mod.__file__
'/Users/car/100daysofcode/real_python/mod.py'
>>> 

When a .py file is imported as a module, Python sets the special dunder 
variable __name__ to the name of the module. However, if a file is run 
as a standalone script, __name__ is (creatively) set to the string '__main__'.
Using this fact, you can discern which is the case at run-time and alter 
behavior accordingly.

For reasons of efficiency, a module is only loaded once per interpreter 
session. That is fine for function and class definitions, which typically
make up the bulk of a module’s contents. But a module can contain 
executable statements as well, usually for initialization. Be aware that 
these statements will only be executed the first time a module is imported.

If you make a change to a module and need to reload it, you need to either
restart the interpreter or use a function called reload() 
from module importlib
"""

s = "If Comrade Napoleon says it, it must be right"
a = [100, 200, 300]


def foo(arg):
    print(f'arg = {arg}')


class Foo:
    pass



# This code output:
# >>> import mod
# If Comrade Napoleon says it, it must be right
# [100, 200, 300]
# arg = bububu
# <mod.Foo object at 0x1069a5590>
# >>> 

# print(s)
print(a)
# foo('bububu')
# x = Foo()
# print(x)

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('bububu')
    x = Foo()
    print(x)