from dlc_list import Node
from dlc_list import DLCList
import unittest


class TestNodes(unittest.TestCase):
    def setUp(self) -> None:
        self.a_node = Node(1)
        self.b_node = Node(2)
        self.c_node = Node(3)
        self.b_node.set_next(self.a_node)
        self.b_node.set_previous(self.c_node)

    def test_node(self):
        self.assertEqual(self.a_node.get_data(), 1)
        self.assertEqual(self.a_node.get_next(), None)
        self.assertEqual(self.a_node.get_previous(), None)
        self.assertEqual(self.b_node.get_next(), self.a_node)
        self.assertEqual(self.b_node.get_previous(), self.c_node)  # Pass


class TestDLCList(unittest.TestCase):
    def setUp(self) -> None:
        self.my_ll = DLCList()  # ll = linked list
        self.my_ll.append(1)
        self.my_ll.append(2)
        self.my_ll.append(3)
        self.my_ll.append(4)

    def test_append(self):
        self.assertEqual(self.my_ll.get_first().get_data(), 1)
        self.assertEqual(self.my_ll.get_last().get_data(), 4)

    def test_remove(self):
        self.my_ll.remove(1)
        self.assertEqual(self.my_ll.get_first().get_data(), 2)
        self.my_ll.remove(4)
        self.assertEqual(self.my_ll.get_last().get_data(), 3)

    def test_size(self):
        self.assertEqual(self.my_ll.get_size(), 4)

    def test_index(self):
        self.assertEqual(self.my_ll.get_at_index(0).get_data(), 1)
        self.assertEqual(self.my_ll.get_at_index(3).get_data(), 4)
        self.assertEqual(self.my_ll.get_index(1), 0)
        self.assertEqual(self.my_ll.get_index(4), 3)

    def test_pop(self):
        self.assertEqual(self.my_ll.pop(), 4)
        self.assertEqual(self.my_ll.pop(), 3)

    def test_insert(self):
        self.my_ll.insert(2, 10)
        self.assertEqual(self.my_ll.get_index(10), 2)
