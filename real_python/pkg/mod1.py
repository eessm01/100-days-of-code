"""
By the way,  __all__ can be defined in a module as well and serves the same
purpose: to control what is imported with import *.

For a module, when __all__ is not defined, import * imports everything 
(except—you guessed it—names starting with an underscore).
"""

__all__ = ['foo']


def foo():
    # from pkg import A
    print('[mod1] foo()')


class Foo:
    pass