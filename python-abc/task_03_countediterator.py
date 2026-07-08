#!/usr/bin/python3
"""Module defining CountedIterator, an iterator that counts its items."""


class CountedIterator:
    """Wrap an iterable and count how many items have been fetched."""

    def __init__(self, iterable):
        """Initialize the iterator and the item counter.

        Args:
            iterable: Any iterable to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item and increment the counter.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated over so far."""
        return self.count
