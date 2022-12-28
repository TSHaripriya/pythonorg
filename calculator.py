import calc
import unittest

class testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,22),32)
        self.assertEqual(calc.add(10.2,17.0),27.2)
    def test_sub(self):
        self.assertEqual(calc.sub(19,7),12)
        self.assertAlmostEqual(calc.sub(22.99,4.71),18.28)
    def test_mul(self):
        self.assertEqual(calc.mul(4,5),21)
        self.assertAlmostEqual(calc.mul(2.0,3.0),6.0)
    def test_equ(self):
        self.assertEqual(calc.equ(5,5),True)
        self.assertEqual(calc.equ(6.6,6.6),True)
    def test_nequ(self):
        self.assertEqual(calc.nequ(5,8),True)
        self.assertEqual(calc.nequ(6.6,6.9),True)
    def test_true(self):
        self.assertEqual(calc.true(True),True)
    def test_false(self):
        self.assertEqual(calc.false(False),False)
    def test_per(self):
        self.assertEqual(calc.per(887,1000),88.7)



if __name__ == "__main__":
    unittest.main(verbosity=2)