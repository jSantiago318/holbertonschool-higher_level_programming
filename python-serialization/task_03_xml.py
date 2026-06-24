#!/usr/bin/python3
"""Module for serializing and deserializing a dictionary with XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into XML and save it to a file.

    Each key/value pair becomes a child element of a <data> root, where
    the tag is the key and the text is the value.

    Args:
        dictionary: The Python dictionary to serialize.
        filename: The path of the output XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Read XML data from a file and return it as a dictionary.

    Args:
        filename: The path of the input XML file.

    Returns:
        A dictionary reconstructed from the XML elements.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
