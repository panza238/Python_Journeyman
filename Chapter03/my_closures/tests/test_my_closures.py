"""Tests written for the my_closures module"""
import unittest
from my_closures.closures import first_class_function


class MyClosuresTests(unittest.TestCase):
    """Tests for my_closures module"""

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_closure_ok(self):
        fn = first_class_function()
        self.assertTrue(callable(fn))


if __name__ == "__main__.py":
    unittest.main()
