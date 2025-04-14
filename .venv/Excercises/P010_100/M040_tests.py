import unittest
from M040_Portokosten import ShippingCostCalculator

class ShippingCosCalculator(unittest.TestCase):
    def test_calculate_shipping_cost(self):
        calculator = ShippingCostCalculator()
        cost1 = calculator.calculate(20.34)
        cost2 = calculator.calculate(55.55)
        cost3 = calculator.calculate(84.45)
        cost4 = calculator.calculate(104.43)
        self.assertEqual(cost1, 3.99)
        self.assertEqual(cost2, 2.99)
        self.assertEqual(cost3, 1.99)
        self.assertEqual(cost4, 0)

if __name__ == '__main__':
    unittest.main()
