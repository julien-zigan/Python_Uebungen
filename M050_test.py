import unittest
from M050_Quadratzahlen import list_squares_under


class TestQuadratzahlen(unittest.TestCase):
    def test_list_squares_under(self):
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81]
        self.assertListEqual(expected, list_squares_under(100))


if __name__ == '__main__':
    unittest.main()
