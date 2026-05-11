#!/usr/bin/python3

def islower(c):
    """Return True if character c is lowercase letter, else False."""
    if not isinstance(c, str) or len(c) != 1:
        return False
    o = ord(c)
    return ord('a') <= o <= ord('z')
