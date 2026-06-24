#!/usr/bin/python3
"""Module that converts CSV data into a JSON file."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its contents to data.json.

    Each CSV row is converted to a dictionary keyed by the header row,
    and the resulting list of dictionaries is serialized to data.json.

    Args:
        csv_filename: The path of the input CSV file.

    Returns:
        True if the conversion succeeded, False otherwise (e.g. the file
        does not exist).
    """
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))
    except FileNotFoundError:
        return False

    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)
    return True
