import unittest
from M010_Zwei_Zahlen_genau_vergleichen import Comparator


class TestComparator(unittest.TestCase):
    def test_max_of(self):
        comparator = Comparator()
        self.assertEqual(comparator.max_of(1, 1), 0)
        self.assertEqual(comparator.max_of(1, 2), -1)
        self.assertEqual(comparator.max_of(2, 1), 1)


if __name__ == '__main__':
    unittest.main()
