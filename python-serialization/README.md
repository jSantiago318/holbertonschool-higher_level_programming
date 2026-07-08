# Python - Serialization

This directory explores **serialization** in Python: converting data structures and
objects into formats that can be stored or transmitted, then reconstructed later.

## Concepts covered

- Serializing and deserializing dictionaries with JSON (`json.dump`, `json.load`)
- Serializing custom objects with `pickle`
- Converting between formats (e.g. CSV to JSON)
- Working with XML serialization

## Files

| File | Description |
| --- | --- |
| `task_00_basic_serialization.py` | Serialize a dict to a JSON file and deserialize it back |
| `task_01_pickle.py` | `CustomObject` that serializes/deserializes itself with `pickle` |
| `task_02_csv.py` | `convert_csv_to_json(csv_filename)` — converts a CSV file to `data.json` |
| `task_03_xml.py` | Serialize/deserialize a dict to and from XML with `ElementTree` |

## Requirements

- Files are interpreted with `python3` (3.8+)
- Code follows `pycodestyle`
- All modules and functions are documented

## Author

Holberton School / Higher-Level Programming track
