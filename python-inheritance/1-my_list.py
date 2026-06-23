#!/usr/bin/python3
"""Module that defines MyList, a list subclass that can print sorted."""


class MyList(list):
    """A list subclass with a helper to print its elements sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
