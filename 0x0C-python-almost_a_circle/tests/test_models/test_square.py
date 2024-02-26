#!/usr/bin/python3
"""Defines the unittest of the Square class"""

import unittest
from models.square import Square
from models.base import Base


class TestSquareInit(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquareSize(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquareArea(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquareUpdateArgs(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))


class TestSquareToDic(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
