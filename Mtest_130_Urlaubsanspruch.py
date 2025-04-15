from unittest import TestCase
from M130_Urlaubsanspruch import vacation_entitlement

class Test(TestCase):
    def test_vacation_entitlement(self):
        self.assertEqual(26, vacation_entitlement(20, 1))
        self.assertEqual(31, vacation_entitlement(20, 1,True))
        self.assertEqual(30, vacation_entitlement(16, 1))
        self.assertEqual(35, vacation_entitlement(16, 1,True))
        self.assertEqual(28, vacation_entitlement(60, 1))
        self.assertEqual(33, vacation_entitlement(60, 1,True))
        self.assertEqual(26 + 2, vacation_entitlement(20, 11))
        self.assertEqual(31 + 2, vacation_entitlement(20, 11, True))
        self.assertEqual(30 + 2, vacation_entitlement(16, 11))
        self.assertEqual(35 + 2, vacation_entitlement(16, 11, True))
        self.assertEqual(28 + 2, vacation_entitlement(60, 11))
        self.assertEqual(33 + 2, vacation_entitlement(60, 11, True))
