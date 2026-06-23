#!/usr/bin/python3
"""Module that defines a Rectangle based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle defined by a validated width and height."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle (positive integer).
            height: The height of the rectangle (positive integer).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
