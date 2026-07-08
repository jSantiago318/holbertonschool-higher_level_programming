#!/usr/bin/python3
"""Module that defines a Square based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, a rectangle with four equal sides."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The length of the square's sides (positive integer).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
