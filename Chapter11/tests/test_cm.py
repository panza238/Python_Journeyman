"""Testing my context manager"""
import unittest
from unittest import TestCase
from context_managers.context_manager import LoggingContextManager  # Make sure to set PythonPath correctly!


class TestCM(TestCase):
    """Context manager testing class"""

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_cm(self):
        print("\nStarting test_cm")
        with LoggingContextManager() as cm:
            # DO NOTHING
            pass

    def test_enter(self):
        print("\nStarting test_enter")
        enter_return = "This text is bound to the reference in the as clause"
        with LoggingContextManager() as cm:
            self.assertEqual(enter_return, str(cm))

    def test_exit_success(self):
        print("\nStarting test_exit_success")
        with LoggingContextManager() as cm:
            print(cm)

    def test_exit_fail(self):
        print("\nStarting test_exit_fail")
        # The assertRaises is a context manager itself!!
        # Here I am using multiple context managers
        with self.assertRaises(ValueError) as t, LoggingContextManager() as cm:
            raise ValueError("Test-generated exception")


if __name__ == "__main__":
    unittest.main()
