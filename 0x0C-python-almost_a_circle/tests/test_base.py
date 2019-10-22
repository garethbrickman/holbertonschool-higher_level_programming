#!/usr/bin/python3
"""Unittest class TestBase
"""
import unittest
from models.base import Base


class Test(unittest.TestCase):
    """ Class for testing Base
    """
    def setUp(self):
        Base._reset_nb_objects()

    def test_id_assignment(self):
        """ Tests first id assignment
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_increment(self):
        """ Tests id increment
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_override(self):
        """ Tests if id arg overrides increment
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_id_reverts(self):
        """ Tests if id increment reverts after override
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(33)
        self.assertEqual(b3.id, 33)
        b4 = Base()
        self.assertEqual(b4.id, 3)
