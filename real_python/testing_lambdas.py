import unittest

"""Real Python. How to Use Python Lambda Functions

Python lambdas can be tested similary to regular functions. It's
possible to use both unittest and doctest.
"""

addtwo = lambda x: x + 2
addtwo.__doc__ = """Add 2 to a number.
    >>> addtwo(2)
    4
    >>> addtwo(2.2)
    4.2
    >>> addtwo(3)  # Should fail
    6
    """

class LambdaTest(unittest.TestCase):

    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)

    def test_add_three(self):
        # Should fail
        self.assertEqual(addtwo(3), 5)


if __name__ == "__main__":
    import doctest

    unittest.main(verbosity=2)
    # doctest.testmod(verbose=True)