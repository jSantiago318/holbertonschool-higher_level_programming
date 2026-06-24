# Python - Input/Output

This directory covers **file I/O** and **serialization** in Python: reading and
writing text files, and converting objects to and from JSON.

## Concepts covered

- Reading text files with the `with` statement (context managers)
- Writing and appending to files
- Serializing Python objects to JSON (`json.dumps`, `json.dump`)
- Deserializing JSON back into Python objects (`json.loads`, `json.load`)
- Converting custom class instances to/from dictionaries

## Files

| File | Description |
| --- | --- |
| `0-read_file.py` | `read_file(filename="")` — reads a UTF-8 text file and prints it to stdout |
| `1-write_file.py` | `write_file(filename="", text="")` — writes a string to a UTF-8 file, returns chars written |
| `2-append_write.py` | `append_write(filename="", text="")` — appends a string to a UTF-8 file, returns chars added |
| `3-to_json_string.py` | `to_json_string(my_obj)` — returns the JSON string representation of an object |
| `4-from_json_string.py` | `from_json_string(my_str)` — returns the Python object represented by a JSON string |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)` — writes an object to a file as JSON |
| `6-load_from_json_file.py` | `load_from_json_file(filename)` — creates an object from a JSON file |
| `7-add_item.py` | Script that adds CLI arguments to a list persisted in `add_item.json` |
| `8-class_to_json.py` | `class_to_json(obj)` — returns a class instance's attributes as a serializable dict |

## Requirements

- Files are interpreted with `python3` (3.8+)
- The first line of every file is `#!/usr/bin/python3`
- Code follows `pycodestyle`
- All modules and functions are documented
- The `with` statement is used for all file operations

## Author

Holberton School / Higher-Level Programming track
