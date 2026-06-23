#!/usr/bin/python3
"""Module that provides a function to list an object's attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the object's attribute and method names.
    """
    return dir(obj)
