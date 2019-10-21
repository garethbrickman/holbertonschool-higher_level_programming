#!/usr/bin/python3
"""Unittest class for Rectangle)
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ Class for testing Rectangle
    """

    """ Tests __str__
    """
    def test_str_override(self):
        """ Tests if __str__ return overrides
        """
        from io import StringIO
        from contextlib import redirect_stdout
        import io
        r1 = Rectangle(4, 6, 2, 1, 12)
        f = io.StringIO()
        f2 = io.StringIO()
        with redirect_stdout(f):
            print(r1.__str__())
        with redirect_stdout(f2):
            print("[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(f, f2)

    """ Tests area method
    """
    # def test_area_meth(self):
    #     r1 = Rectangle(3, 2)
    #     self.assertEqual(r1.area(), 6)

    # def test_area_print(self):
    #     from io import StringIO
    #     from contextlib import redirect_stdout
    #     import io
    #     r1 = Rectangle(3, 2)
    #     f = io.StringIO()
    #     f2 = io.StringIO()
    #     with redirect_stdout(f):
    #         print(r1.area())
    #     with redirect_stdout(f2):
    #         print(6)
    #     self.assertEqual(f, f2)

    # """ Tests validation
    # """
    # def test_int_validate(self):
    #     """ Tests if input is int
    #     """
    #     with self.assertRaises(TypeError) as cm:
    #         r1 = Rectangle(10, "2")
    #     self.assertEqual(str(cm.exception), "height must be an integer")

    # def test_greater_validate(self):
    #     """ Tests if input is > 0
    #     """
    #     with self.assertRaises(ValueError) as cm:
    #         r1 = Rectangle(10, 2)
    #         r1.width = -10
    #     self.assertEqual(str(cm.exception), "width must be > 0")

    # def test_greater_equal_validate(self):
    #     """ Tests if input is >= 0
    #     """
    #     with self.assertRaises(ValueError) as cm:
    #         r1 = Rectangle(10, 2, 3, -1)
    #     self.assertEqual(str(cm.exception), "y must be >= 0")

    # """ Tests attribute assignment
    # """
    # def test_width_assign(self):
    #     """ Tests width attribute
    #     """
    #     r1 = Rectangle(1, 2)
    #     self.assertEqual(r1.width, 1)

    # def test_height_assign(self):
    #     """ Tests height attribute
    #     """
    #     r1 = Rectangle(1, 2)
    #     self.assertEqual(r1.height, 2)

    # def test_x_assign(self):
    #     """ Tests x attribute
    #     """
    #     r1 = Rectangle(1, 2, 3, 4)
    #     self.assertEqual(r1.x, 3)

    # def test_y_assign(self):
    #     """ Tests y attribute
    #     """
    #     r1 = Rectangle(1, 2, 3, 4)
    #     self.assertEqual(r1.y, 4)

    # """ Tests for id/nb_objects
    # """
    # def setUp(self):
    #     Base._reset_nb_objects()

    # def test_rec_id_first(self):
    #     """ Tests first id assignment
    #     """
    #     r1 = Rectangle(10, 2)
    #     self.assertEqual(r1.id, 1)

    # def test_rec_id_increment(self):
    #     """ Tests id increment
    #     """
    #     r1 = Rectangle(2, 10)
    #     r2 = Rectangle(2, 10)
    #     self.assertEqual(r2.id, 2)

    # def test_rec_override(self):
    #     """ Tests if id arg overrides increment
    #     """
    #     r2 = Rectangle(2, 10)
    #     r3 = Rectangle(10, 2, 0, 0, 12)
    #     self.assertEqual(r3.id, 12)

    # def test_rec_id_reverts(self):
    #     """ Tests if id increment reverts after override
    #     """
    #     r1 = Rectangle (2, 10)
    #     r2 = Rectangle(2, 10)
    #     r3 = Rectangle(10, 2, 0, 0, 12)
    #     r4 = Rectangle(9, 3)
    #     self.assertEqual(r4.id, 3)
