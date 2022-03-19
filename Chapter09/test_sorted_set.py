"""Tests for the SortedSet module"""
import unittest
from sorted_set import SortedSet


class TestSortedSet(unittest.TestCase):
    """Test SortedSet !"""

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_instantiate_empty(self):
        s = SortedSet()

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([4, 3, 2, 1])

    def test_with_duplicates(self):
        s = SortedSet([4, 3, 2, 2, 1, 1])

    def test_from_iterator(self):
        def gen4221():
            yield 4
            yield 2
            yield 2
            yield 1

        s = SortedSet(gen4221())


class TestContainerProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.s = SortedSet([1, 4, 2, 3, 3])

    def tearDown(self) -> None:
        pass

    def test_in(self):
        isin: bool = 1 in self.s
        self.assertTrue(isin)

    def test_not_in(self):
        notin: bool = 5 in self.s
        self.assertFalse(notin)


class TestIterableProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.seq = [1, 2, 3, 3]
        self.s = SortedSet(self.seq)

    def tearDown(self) -> None:
        pass

    def test_iteration(self):
        s = iter(self.s)
        s0 = next(s)
        next(s)
        next(s)
        s3 = next(s)

        self.assertEqual(s0, 1)
        self.assertEqual(s3, 3)
        # assertRaises returns a context manager! That's why we can use it with a with statement.
        with self.assertRaises(StopIteration):
            next(s)


class TestSequenceProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.seq = [ 1, 3, 4, 7, 9]
        self.s = SortedSet(self.seq)

    def tearDown(self) -> None:
        pass

    def test_index_zero(self):
        s0 = self.s[0]
        self.assertEqual(s0, 1)

    def test_index_four(self):
        s4 = self.s[4]
        self.assertEqual(s4, 9)

    def test_index_error(self):
        with self.assertRaises(IndexError):
            index_error = self.s[5]

    def test_slice_from_start(self):
        s_3 = self.s[:3]
        # This works ONLY because self.seq is SORTED. Otherwise, the slice wouldn't work
        self.assertEqual(s_3, SortedSet(self.seq[:3]))

    def test_slice_arbitrary(self):
        s2_4 = self.s[2:4]
        # This works ONLY because self.seq is SORTED. Otherwise, the slice wouldn't work
        self.assertEqual(s2_4, SortedSet(self.seq[2:4]))


class TestEqualityProtocol(unittest.TestCase):

    def setUp(self) -> None:
        self.seq1 = [7, 2, 1, 1, 9]
        self.seq2 = [7, 2, 1, 1, 9]
        self.seq3 = [7, 2, 1, 1, 0]
        self.s1 = SortedSet(self.seq1)
        self.s3 = SortedSet(self.seq3)

    def tearDown(self) -> None:
        pass

    def test_positive_equality(self):
        self.assertTrue(SortedSet(self.seq1) == SortedSet(self.seq2))

    def test_negative_equality(self):
        self.assertFalse(SortedSet(self.seq1) == SortedSet(self.seq3))


if __name__ == "__main__":
    unittest.main()
