#!/usr/bin/python3
"""function writes an Object to a text file, using a JSON representation
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""

    with open(filename, "w") as f:
        dump(my_obj, f)
