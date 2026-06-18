#!/usr/bin/python3
"""Module for add_integer function.

Adds two integers or floats cast to integers.
Raises TypeError if either argument is not an integer or float.
"""


def add_integer(a, b=98):
    """Adds two integers.
    Raises TypeError if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
