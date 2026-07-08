#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """Base class for geometry-related classes."""

    def area(self):
        """Raise an Exception because area is not implemented.

        Raises:
            Exception: Always, with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
