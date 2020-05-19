"""
Note: Much of the Python documentation states that an __init__.py file 
must be present in the package directory when creating a package. 
This was once true. It used to be that the very presence of __init__.py 
signified to Python that a package was being defined. The file could 
contain initialization code or even be empty, but it had to be present.

Starting with Python 3.3, Implicit Namespace Packages were introduced. 
These allow for the creation of a package without any __init__.py file. 
Of course, it can still be present if package initialization is needed. 
But it is no longer required.

For a package, when __all__ is not defined, import * does not import 
anything.
"""


# print(f'Invoking __init__.py for {__name__}')
# A = ['quux', 'corge', 'grault']
# import pkg.mod1, pkg.mod2
__all__ = [
    'mod1',
    'mod2',
    'mod3',
    'mod4'
]