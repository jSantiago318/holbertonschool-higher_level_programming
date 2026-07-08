#!/usr/bin/python3
"""Module that defines a BaseGeometry class with integer validation."""


class BaseGeometry:
    """Base class for geometry-related classes."""

    def area(self):
        """Raise an Exception because area is not implemented.

        Raises:
            Exception: Always, with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name: The label used in error messages (assumed to be a string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
