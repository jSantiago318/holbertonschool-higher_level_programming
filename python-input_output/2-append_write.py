#!/usr/bin/python3
"""Module that provides a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return characters added.

    The file is created if it does not exist.

    Args:
        filename: The path of the file to append to (defaults to "").
        text: The string to append to the file (defaults to "").

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
