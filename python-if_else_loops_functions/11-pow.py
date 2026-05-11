#!/usr/bin/python3

def pow(a, b):
    """Compute a to the power of b and return the value."""
    if b == 0:
        return 1
    negative = b < 0
    exp = -b if negative else b
    result = 1
    for _ in range(exp):
        result *= a
    if negative:
        return 1 / result
    return result
