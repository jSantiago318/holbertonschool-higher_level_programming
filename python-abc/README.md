# Python - Abstract Base Classes

This directory explores **abstract base classes (ABCs)**, **duck typing**, **mixins**,
and **interfaces** in Python — tools for defining contracts that subclasses must
fulfil and for sharing behavior across unrelated class hierarchies.

## Concepts covered

- Declaring abstract base classes with the `abc` module (`ABC`, `@abstractmethod`)
- Forcing subclasses to implement required methods (instantiating an incomplete
  subclass raises `TypeError`)
- Duck typing and informal interfaces
- Mixins for composable, reusable behavior
- Overriding special (dunder) methods

## Files

| File | Description |
| --- | --- |
| `task_00_abc.py` | Abstract `Animal` class with `Dog` and `Cat` subclasses implementing `sound` |
| `task_01_duck_typing.py` | Abstract `Shape` with `Circle`/`Rectangle` and a duck-typed `shape_info` function |
| `task_02_verboselist.py` | `VerboseList`, a `list` subclass that prints a message on append/extend/remove/pop |
| `task_03_countediterator.py` | `CountedIterator`, an iterator that counts how many items have been fetched |

## Requirements

- Files are interpreted with `python3` (3.8+)
- Code follows `pycodestyle`
- All modules, classes, and methods are documented

## Author

Holberton School / Higher-Level Programming track
