#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the new square.
        """
        self.__size = size
