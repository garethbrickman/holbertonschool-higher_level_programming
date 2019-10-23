#!/usr/bin/python3
"""Unittest class for Square
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """ Class for testing Square
    """
    def setUp(self):
        """ Setup tests
        """
        Base._reset_nb_objects()

    """ Tests dictionary to instance
    """
    # def test_dict_to_instance(self):
    #     """ Tests if create method words
    #     """
    #     from io import StringIO
    #     import io
    #     import contextlib
    #     r1 = Square(3)
    #     r1_dictionary = r1.to_dictionary()
    #     r2 = Square.create(**r1_dictionary)
    #     temp_stdout = io.StringIO()
    #     with contextlib.redirect_stdout(temp_stdout):
    #         print(r2)
    #     output = temp_stdout.getvalue()
    #     self.assertEqual(output, '[Square] (1) 0/0 - 3\n')

    # def test_dict_instance_bool(self):
    #     """ Tests if bool is False
    #     """
    #     r1 = Square(3, 5, 1)
    #     r1_dictionary = r1.to_dictionary()
    #     r2 = Square.create(**r1_dictionary)
    #     self.assertNotEqual(r1, r2)

    """ Tests dictionary methods
    """
    def test_to_dictionary(self):
        """ Tests if to_dictionary works
        """
        r1 = Square(10, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square(1, 1)
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
        r1 = Square(5)
        r1.update(10)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (10) 0/0 - 5\n')

    def test_tricky_args__update(self):
        """ Tests if tricky args update method works
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Square(5)
        r1.update(1, 2, 3, 4)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 3/4 - 2\n')

    def test_kwargs_update(self):
        """ Tests if kwargs update method works
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Square(5)
        r1.update(size=7)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (1) 0/0 - 7\n')

    def test_tricky_kwargs_update(self):
        """ Tests if tricky kwargs update method works
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Square(5)
        r1.update(size=7, id=89, y=1, x=12)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(r1)
        output = temp_stdout.getvalue()
        self.assertEqual(output, '[Square] (89) 12/1 - 7\n')

    """ Tests print output
    """
    def test_basic_print(self):
        """ Tests if basic square prints
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Square(3)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '###\n###\n###\n')

    def test_x2y2_print(self):
        """ Tests if x2y2 square prints
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Square(2, 2)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '  ##\n  ##\n')

    def test_x1y0_print(self):
        """ Tests if x1y3 square prints
        """
        from io import StringIO
        import io
        import contextlib
        r1 = Square(3, 1, 3)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            r1.display()
        output = temp_stdout.getvalue()
        self.assertEqual(output, '\n\n\n ###\n ###\n ###\n')

    """ Tests __str__
    """
    def test_str_override(self):
        """ Tests if __str__ return overrides
        """
        from io import StringIO
        import io
        import contextlib
        s1 = Square(5)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        assert output == "[Square] (1) 0/0 - 5"

    """ Tests area method
    """
    def test_area_meth(self):
        """ Tests if area method works
        """
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_area_print(self):
        """ Tests if area prints
        """
        from io import StringIO
        import io
        import contextlib
        s1 = Square(3)
        temp_stdout = io.StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1.area())
        output = temp_stdout.getvalue().strip()
        assert output == "9"

    """ Tests validation
    """
    def test_int_validate(self):
        """ Tests if input is int
        """
        with self.assertRaises(TypeError) as cm:
            s1 = Square("2")
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_greater_validate(self):
        """ Tests if input is > 0
        """
        with self.assertRaises(ValueError) as cm:
            r1 = Square(10)
            r1.width = -10
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_greater_equal_validate(self):
        """ Tests if input is >= 0
        """
        with self.assertRaises(ValueError) as cm:
            r1 = Square(10, 2, -3)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    """ Tests attribute assignment
    """
    def test_width_assign(self):
        """ Tests width attribute
        """
        r1 = Square(1, 2)
        self.assertEqual(r1.width, 1)

    def test_height_assign(self):
        """ Tests height attribute
        """
        r1 = Square(2, 3)
        self.assertEqual(r1.height, 2)

    def test_x_assign(self):
        """ Tests x attribute
        """
        r1 = Square(1, 2, 3, 4)
        self.assertEqual(r1.x, 2)

    def test_y_assign(self):
        """ Tests y attribute
        """
        r1 = Square(1, 2, 3)
        self.assertEqual(r1.y, 3)

    """ Tests for id/nb_objects
    """

    def test_rec_id_first(self):
        """ Tests first id assignment
        """
        r1 = Square(10)
        self.assertEqual(r1.id, 1)

    def test_rec_id_increment(self):
        """ Tests id increment
        """
        r1 = Square(2)
        r2 = Square(2)
        self.assertEqual(r2.id, 2)

    def test_rec_override(self):
        """ Tests if id arg overrides increment
        """
        r2 = Square(2, 10)
        r3 = Square(10, 2, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rec_id_reverts(self):
        """ Tests if id increment reverts after override
        """
        r1 = Square(2, 10)
        r2 = Square(2, 10)
        r3 = Square(10, 2, 0, 12)
        r4 = Square(9, 3)
        self.assertEqual(r4.id, 3)
