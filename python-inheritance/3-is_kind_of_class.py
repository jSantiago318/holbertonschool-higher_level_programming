#!/usr/bin/python3
"""Module that checks if an object is an instance of a class or subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it.

    Args:
        obj: The object to check.
        a_class: The class to match against, including its subclasses.

    Returns:
        True if isinstance(obj, a_class), otherwise False.
    """
    return isinstance(obj, a_class)
