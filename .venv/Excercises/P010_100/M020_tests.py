import unittest

from M020_Begrüßung import Greeter

class TestGreeter(unittest.TestCase):
    def test_greet(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet(2), "Gute Nacht")
        self.assertEqual(greeter.greet(8), "Guten Morgen")
        self.assertEqual(greeter.greet(13), "Mahlzeit")
        self.assertEqual(greeter.greet(16), "Guten Nachmittag")
        self.assertEqual(greeter.greet(20), "Guten Abend")
        self.assertEqual(greeter.greet(23), "Gute Nacht")

    def test_greet2(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet2(2), "Gute Nacht")
        self.assertEqual(greeter.greet2(8), "Guten Morgen")
        self.assertEqual(greeter.greet2(13), "Mahlzeit")
        self.assertEqual(greeter.greet2(16), "Guten Nachmittag")
        self.assertEqual(greeter.greet2(20), "Guten Abend")
        self.assertEqual(greeter.greet2(23), "Gute Nacht")


if __name__ == '__main__':
    unittest.main()
