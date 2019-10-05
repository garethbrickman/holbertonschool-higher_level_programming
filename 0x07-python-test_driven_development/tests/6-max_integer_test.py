#!/usr/bin/python3
"""Unittest for max_integer([..])



"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for testing max_integer """

    def test_if_list(self):
        self.normlist = [1, 2, 3, 4]
        self.assertIsInstance(self.normlist, list)

    def test_builtin_max(self):
        self.toughlist = [1, 90, 2, 13, 34, 5, -13, 3]
        self.assertEqual(max_integer(self.toughlist), max(self.toughlist))

    def test_empty_list(self):
        self.emptylist = []
        self.assertIsNone(max_integer(self.emptylist))

    def test_int_list(self):
        self.intlist = [2, 3.3, 4]
        self.assertEqual(all(isinstance(x, int) for x in self.intlist), False)
