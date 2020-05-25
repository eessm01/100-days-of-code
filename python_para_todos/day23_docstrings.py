#-* coding: utf-8 --*
"""
Yo can make life easier for yourself by commenting your own code 
properly. Even if no one else will ever see it, you'll see it, 
and that's enough reason to make it right. You're a developer
after all. so your code should be easy for you to understand as
well.
"""

def haz_algo(arg):
    """Este es el docstring de la función"""
    print arg



if __name__ == '__main__':
    print haz_algo.__doc__

    haz_algo.__doc__ = """Este es el nuevo docstring."""

    print haz_algo.__doc__
