#!/usr/bin/python3
"""function write_file"""


def write_file(filename="", text=""):
    """return the number the char inserted"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
