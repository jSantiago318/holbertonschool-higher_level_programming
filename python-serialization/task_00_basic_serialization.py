#!/usr/bin/python3
"""Module for basic serialization of a dictionary to and from a JSON file."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to a file.

    If the file already exists, its contents are replaced.

    Args:
        data: A Python dictionary with the data to serialize.
        filename: The path of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file.

    Args:
        filename: The path of the input JSON file.

    Returns:
        A Python dictionary with the deserialized JSON data.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
