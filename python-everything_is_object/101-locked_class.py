#!/usr/bin/python3
"""Defines a class that locks down dynamic instance attributes."""


class LockedClass:
    """Only allows the instance attribute ``first_name`` to be created."""

    __slots__ = ("first_name",)
