"""Contextlib for context managers"""
import unittest
from unittest import TestCase

from context_managers.contextlib_ex import my_cm


class TestMyCM(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_my_cm(self):
        print("\ntesting test_my_cm")
        with my_cm("hello") as cm:
            print(cm)

    def test_my_cm_fail(self):
        print("\ntesting test_my_cm_fail")

        with self.assertRaises(ValueError) as exc, my_cm('fail var') as cm:
            print(cm)
            raise ValueError


if __name__ == "__main__":
    unittest.main()
