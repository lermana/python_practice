from fractions import Fraction

import unittest


class TestFractions(unittest.TestCase):

    def test_fraction_construction(self):
        self.assertEqual(Fraction(0, 4), 0)
        self.assertEqual(Fraction(4, 1), 4)
        self.assertEqual(Fraction(4, -1), Fraction(-4, 1))
        self.assertRaises(ZeroDivisionError, lambda: Fraction(4, 0))
        self.assertRaises(TypeError, lambda: Fraction(.5, 1))
        self.assertRaises(TypeError, lambda: Fraction(1, .5))
        self.assertRaises(TypeError, lambda: Fraction('a', 4))    
        self.assertRaises(TypeError, lambda: Fraction(4, 'a'))

    def test_fraction_addition(self):
        self.assertEqual(Fraction(3, 5) + Fraction(2, 7), Fraction(31, 35))
        self.assertEqual(Fraction(3, 5) + Fraction(7, 5), 2)
        self.assertEqual(Fraction(3, 5) + Fraction(2, 7), 
        				 Fraction(2, 7) + Fraction(3, 5))
        self.assertEqual(Fraction(4, 8) + Fraction(3, 2) + Fraction(5, 10), 
        				 Fraction(5, 2))
        self.assertEqual(Fraction(3, 5) + 2, Fraction(13, 5))
        self.assertEqual(2 + Fraction(3, 5), Fraction(13, 5))
        self.assertEqual(Fraction(3, 5) + 0, Fraction(3, 5))
        self.assertRaises(TypeError, lambda: Fraction(3, 5) + .5)
        self.assertRaises(TypeError, lambda: Fraction(3, 5) + 'a')

    def test_fraction_subtraction(self):
        self.assertEqual(Fraction(3, 5) - Fraction(2, 7), Fraction(11, 35))
        self.assertEqual(Fraction(2, 7) - Fraction(3, 5), Fraction(-11, 35))
        self.assertEqual(Fraction(3, 5) - Fraction(8, 5), -1)
        self.assertEqual(Fraction(4, 8) - Fraction(3, 2) - Fraction(5, 10), 
        				 Fraction(-3, 2))
        self.assertEqual(Fraction(3, 5) - 2, Fraction(-7, 5))
        self.assertEqual(2 - Fraction(3, 5), Fraction(7, 5))
        self.assertEqual(Fraction(3, 5) - 0, Fraction(3, 5))
        self.assertEqual(Fraction(3, 5) - (-Fraction(2, 7)), Fraction(31, 35))
        self.assertEqual(Fraction(3, 5) + (-Fraction(2, 7)), Fraction(11, 35))
        self.assertRaises(TypeError, lambda: Fraction(3, 5) - .5)
        self.assertRaises(TypeError, lambda: Fraction(3, 5) - 'a')

    def test_fraction_multiplication(self):
        self.assertEqual(Fraction(3, 5) * 2, Fraction(6, 5))
        self.assertEqual(2 * Fraction(3, 5), Fraction(6, 5))
        self.assertEqual(Fraction(3, 5) * Fraction(2, 7), Fraction(6, 35))
        self.assertEqual(Fraction(2, 7) * Fraction(3, 5), Fraction(6, 35))
        self.assertEqual(Fraction(2, 7) * (Fraction(3, 5) * 2), 
        				(Fraction(2, 7) * Fraction(3, 5)) * 2)
        self.assertEqual(Fraction(3, 5) * 0, 0)
        self.assertRaises(TypeError, lambda: Fraction(3, 5) * .5)
        self.assertRaises(TypeError, lambda: Fraction(3, 5) * 'a')

    def test_fraction_division(self):
        self.assertEqual(Fraction(3, 5) / 2, Fraction(3, 10))
        self.assertEqual(2 / Fraction(3, 5), Fraction(10, 3))
        self.assertEqual(Fraction(3, 5) / Fraction(2, 7), Fraction(21, 10))
        self.assertEqual(2 / Fraction(3, 5) / Fraction(2, 7), Fraction(35, 3))
        self.assertEqual(2 / (Fraction(3, 5) / Fraction(2, 7)), Fraction(20, 21))
        self.assertEqual(0 / Fraction(3, 5), 0)
        self.assertEqual(Fraction(3, 5) / Fraction(3, 5), 1)
        self.assertRaises(ZeroDivisionError, lambda: Fraction(3, 5) / 0)
        self.assertRaises(TypeError, lambda: Fraction(3, 5) / .5)
        self.assertRaises(TypeError, lambda: Fraction(3, 5) / 'a')

    def test_fracion_comparison(self):
        self.assertTrue(Fraction(1, 6) < Fraction(3, 7))
        self.assertTrue(Fraction(1, 6) <= Fraction(3, 7))
        self.assertTrue(Fraction(1, 6) != Fraction(3, 7))
        self.assertTrue(Fraction(3, 7) >= Fraction(1, 6))
        self.assertTrue(Fraction(3, 7) > Fraction(1, 6))
        self.assertTrue(Fraction(3, 7) < 1)
        self.assertTrue(1 > Fraction(3, 7))
        self.assertTrue(Fraction(3, 5) == .6)
        self.assertTrue(Fraction(3, 7) != .6)
        self.assertFalse(Fraction(1, 6) == Fraction(3, 7))
        self.assertFalse(Fraction(1, 6) > Fraction(3, 7))
        self.assertFalse(Fraction(3, 7) > 1)
        self.assertFalse(Fraction(999, 1000) != .999)


if __name__ == '__main__':
    unittest.main()


