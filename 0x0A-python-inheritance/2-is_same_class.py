#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Args:
        obj (any): object to check
        a_class (any): the class

    Returns:
        bool: True if type of obj eq a_class
    """
    if type(obj) == a_class:
        return True
    return False
