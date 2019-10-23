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
        """ Setup tests
        """
        Base._reset_nb_objects()

    """ Tests dictionary to instance
    """
    def test_dict_to_instance(self):
        """ Tests if create method words
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r2)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 1/0 - 3/5\n')

    def test_dict_instance_bool(self):
        """ Tests if bool is False
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    """ Tests dictionary methods
    """
    def test_to_dictionary(self):
        """ Tests if to_dictionary works
        """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    """ Tests attribute updates
    """
    def test_args_update(self):
        """ Tests if args update method works
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 10/10 - 2/10\n')

    def test_tricky_args__update(self):
        """ Tests if tricky args update method works
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 4/5 - 2/3\n')

    def test_kwargs_update(self):
        """ Tests if kwargs update method works
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (1) 10/10 - 10/1\n')

    def test_tricky_kwargs_update(self):
        """ Tests if tricky kwargs update method works
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, id=89)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Rectangle] (89) 1/3 - 4/2\n')

    """ Tests print output
    """
    def test_basic_print(self):
        """ Tests if basic rectangle prints
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(3, 1)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '###\n')

    def test_x2y2_print(self):
        """ Tests if x2y2 rectangle prints
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(2, 3, 2, 2)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '\n\n  ##\n  ##\n  ##\n')

    def test_x1y0_print(self):
        """ Tests if x1y0 rectangle prints
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(3, 2, 1, 0)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, ' ###\n ###\n')

    """ Tests __str__
    """
    def test_str_override(self):
        """ Tests if __str__ return overrides
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(4, 6, 2, 1, 12)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue().strip()
        assert output == "[Rectangle] (12) 2/1 - 4/6"

    """ Tests area method
    """
    def test_area_meth(self):
        """ Tests if area method works
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area_print(self):
        """ Tests if area prints
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Rectangle(3, 2)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1.area())
        output = temp_stdout.getvalue().strip()
        assert output == "6"

    """ Tests validation
    """
    def test_int_validate(self):
        """ Tests if input is int
        """
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_greater_validate(self):
        """ Tests if input is > 0
        """
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(10, 2)
            r1.width = -10
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_greater_equal_validate(self):
        """ Tests if input is >= 0
        """
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    """ Tests attribute assignment
    """
    def test_width_assign(self):
        """ Tests width attribute
        """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)

    def test_height_assign(self):
        """ Tests height attribute
        """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.height, 2)

    def test_x_assign(self):
        """ Tests x attribute
        """
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.x, 3)

    def test_y_assign(self):
        """ Tests y attribute
        """
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.y, 4)

    """ Tests for id/nb_objects
    """

    def test_rec_id_first(self):
        """ Tests first id assignment
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_rec_id_increment(self):
        """ Tests id increment
        """
        r1 = Rectangle(2, 10)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_rec_override(self):
        """ Tests if id arg overrides increment
        """
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rec_id_reverts(self):
        """ Tests if id increment reverts after override
        """
        r1 = Rectangle(2, 10)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(9, 3)
        self.assertEqual(r4.id, 3)
