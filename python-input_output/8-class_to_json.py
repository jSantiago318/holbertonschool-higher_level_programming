#!/usr/bin/python3
"""Module that builds a JSON-serializable dict from a class instance."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    The returned dictionary contains the instance's attributes, all of which
    are assumed to be simple serializable types (list, dict, str, int, bool).

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary of the object's instance attributes.
    """
    return dict(obj.__dict__)
