import unittest
from radix_sort import RadixSort


class TestSort(unittest.TestCase):
    def setUp(self) -> None:
        self.my_lst = [9, 7, 4, 8, 6]
        self.sort_machine = RadixSort(self.my_lst)

    def testSort(self):
        self.assertEqual(self.sort_machine.radix_sort(), [4, 6, 7, 8, 9])