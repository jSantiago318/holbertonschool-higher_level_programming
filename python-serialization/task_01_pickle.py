#!/usr/bin/python3
"""Module for pickling and unpickling a custom object."""
import pickle


class CustomObject:
    """A custom object that can serialize itself with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject.

        Args:
            name: The object's name (str).
            age: The object's age (int).
            is_student: Whether the object is a student (bool).
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this instance and save it to a file with pickle.

        Args:
            filename: The path of the file to write to.

        Returns:
            None on success or if an error occurs while writing.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject from a pickle file.

        Args:
            filename: The path of the file to read from.

        Returns:
            The deserialized CustomObject, or None if the file does not
            exist or cannot be unpickled.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
        except Exception:
            return None
