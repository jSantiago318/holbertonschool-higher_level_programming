#!/usr/bin/python3
"""Module demonstrating mixins with a Dragon that swims and flies."""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly, and also roar."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
