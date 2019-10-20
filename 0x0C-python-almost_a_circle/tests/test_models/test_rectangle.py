#!/usr/bin/python3
"""Unittest class for Rectangle)
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ Class for testing Rectangle
    """
    def setUp(self):
        Base._reset_nb_objects()

    def test_rec_id_first(self):
        """ Tests first id assignment
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_rec_id_increment(self):
        """ Tests id increment
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
