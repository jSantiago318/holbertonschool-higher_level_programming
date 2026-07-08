#!/usr/bin/python3
"""Module that checks whether an object's class inherits from another."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    The check is True only when a_class is a proper ancestor of obj's
    class; it is False when obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The ancestor class to match against.

    Returns:
        True if obj inherits (directly or indirectly) from a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
