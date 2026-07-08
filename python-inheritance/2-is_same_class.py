#!/usr/bin/python3
"""Module that checks whether an object is exactly of a given class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: The object to check.
        a_class: The class to match against exactly.

    Returns:
        True if type(obj) is a_class, otherwise False.
    """
    return type(obj) is a_class
