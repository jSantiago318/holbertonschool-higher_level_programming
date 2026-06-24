#!/usr/bin/python3
"""Module that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n.

    Each row is built from the previous one: an interior value is the sum
    of the two values above it, and every row begins and ends with 1.

    Args:
        n: The number of rows of the triangle.

    Returns:
        A list of lists of integers, or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev = triangle[-1]
        row = [1]
        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
