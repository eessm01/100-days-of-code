"""
Module contents can be imported from within a function definition. 
In that case, the import does not occur until the function 
is called

However, Python 3 does not allow the indiscriminate 
import * 
syntax from within a function
SyntaxError: import * only allowed at module level
"""

def bar():
    from mod import foo
    foo('courage')


bar()