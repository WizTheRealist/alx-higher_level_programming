#!/usr/bin/python3
"""An object lookup function"""


def lookup(obj):
    """Returns a list of available attributes of an object"""
    return dir(obj)
