import unittest
from postfix import infix_calc


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.infix_1 = "5 * 3 // 6.0"
        self.infix_2 = "2 ** 2"
        self.infix_3 = "(2 * 5) + (3 * 2)"
        self.infix_4 = "2+2*3+4.0"

    def test_math(self):
        self.assertEqual(infix_calc(self.infix_1), 2.0)
        self.assertEqual(infix_calc(self.infix_2), 4.0)
        self.assertEqual(infix_calc(self.infix_3), 16.0)
        self.assertEqual(infix_calc(self.infix_4), 12.0)