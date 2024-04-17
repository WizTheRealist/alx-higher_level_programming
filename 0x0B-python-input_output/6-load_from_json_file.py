#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
from json import load


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""

    with open(filename, 'r') as f:
        return load(f)
