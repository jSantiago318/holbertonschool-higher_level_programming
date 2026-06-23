#!/usr/bin/python3
"""Module defining an abstract Animal class and Dog/Cat subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes.

        This is an abstract method that subclasses must implement.
        """
        pass


class Dog(Animal):
    """Represent a dog."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Represent a cat."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
