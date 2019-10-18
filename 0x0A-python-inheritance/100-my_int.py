#!/usr/bin/python3
"""
     Class for MyInt
"""


class MyInt(int):
    """Defines base class"""

    def __init__(self, int):
        """Instantiation"""
        super().__init__()
        self.int = int
