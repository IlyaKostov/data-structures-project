"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    n1 = Node(5, None)
    n2 = Node('q', n1)

    def test_node(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, 'q')
        self.assertEqual(self.n2.next_node, self.n1)


class TestStackPush(unittest.TestCase):

    stack = Stack()
    stack.push('1')
    stack.push('2')

    def test_push(self):
        self.assertEqual(self.stack.top.data, '2')
        self.assertEqual(self.stack.top.next_node.data, '1')
        self.assertEqual(self.stack.top.next_node.next_node, None)

    def test_push_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.stack.top.next_node.next_node.data

