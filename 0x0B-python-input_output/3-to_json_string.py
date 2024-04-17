#!/usr/bin/python3
"""function returns the JSON representation of an object (string)
"""
from json import dumps


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return dumps(my_obj)
