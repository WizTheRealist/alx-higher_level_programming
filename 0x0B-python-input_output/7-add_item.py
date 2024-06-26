#!/usr/bin/python3
"""Adds item to a json file"""

from sys import argv
from json.decoder import JSONDecodeError


if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file
    file_name = "add_item.json"
    data = []
    try:
        data = load_from_json_file(file_name)
    except (FileNotFoundError, JSONDecodeError):
        pass
    save_to_json_file(data + argv[1:], file_name)
