import unittest
from unittest import TestCase
from M100_Hundealter import man_2_dog_years


class TestDogYears(TestCase):
    def test_man_2_dog_years(self):
        expected = [0, 14, 22, 27, 32, 37, 42, 47, 52, 57]
        for i in range(10):
            self.assertEqual(expected[i], man_2_dog_years(i))

if __name__ == '__main__':
    unittest.main()