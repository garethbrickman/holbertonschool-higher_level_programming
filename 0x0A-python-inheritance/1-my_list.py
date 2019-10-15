#!/usr/bin/python3
"""
     Class for defining list
"""


class MyList(list):
    """Defines base class inheriting from list"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
