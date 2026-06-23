#!/usr/bin/python3
"""Module defining VerboseList, a list that announces its mutations."""


class VerboseList(list):
    """A list subclass that prints a message on each add or remove."""

    def append(self, item):
        """Append an item and announce it."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with an iterable and announce the count."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Announce the item then remove its first occurrence."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Announce the item at index then pop and return it."""
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
