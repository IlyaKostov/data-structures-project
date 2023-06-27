"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Queue, Node


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_queue_str(self):
        self.assertEqual(str(self.queue), 'data1\ndata2\ndata3')

    def test_enqueue(self):
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.head.next_node.data, 'data2')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)

    def test_enqueue_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.queue.tail.next_node.data

    def test_dequeue(self):
        data = self.queue.dequeue()
        self.assertEqual(data, 'data1')
        self.assertEqual(self.queue.head.data, 'data2')
        data2 = self.queue.dequeue()
        self.assertEqual(data2, 'data2')
        data3 = self.queue.dequeue()
        self.assertEqual(data3, 'data3')
        self.assertEqual(self.queue.head, None)
        data4 = self.queue.dequeue()
        self.assertEqual(data4, None)


class TestNode(unittest.TestCase):

    def setUp(self):
        self.n1 = Node(5, None)
        self.n2 = Node('q', None)

    def test_node(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, 'q')
        self.assertEqual(self.n2.next_node, None)
