#!/usr/bin/python3
"""Module that provides a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return characters written.

    The file is created if it does not exist and overwritten if it does.

    Args:
        filename: The path of the file to write to (defaults to "").
        text: The string to write to the file (defaults to "").

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
