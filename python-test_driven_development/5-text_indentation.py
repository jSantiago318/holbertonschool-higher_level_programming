#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' or ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    buf = ""
    for char in text:
        buf += char
        if char in ".?:":
            print(buf.strip())
            print()
            buf = ""
    if buf.strip():
        print(buf.strip(), end="")
