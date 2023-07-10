"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.ll = LinkedList()

    def test_linked_list_str(self):
        self.assertEqual(self.ll.head, None)
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.assertEqual(str(self.ll), "{'id': 1} -> {'id': 2} -> None")

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 2})
        self.assertEqual(self.ll.head.data, {'id': 2})
        self.assertEqual(self.ll.head.next_node, None)
        self.assertEqual(self.ll.tail.data, {'id': 2})
        self.assertEqual(self.ll.tail.next_node, None)
        self.ll.insert_at_end({'id': 3})
        self.assertEqual(self.ll.head.data, {'id': 2})
        self.assertEqual(self.ll.head.next_node.data, {'id': 3})
        self.assertEqual(self.ll.tail.next_node, None)
        self.assertEqual(self.ll.tail.data, {'id': 3})

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_beginning({'id': 0})
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.head.next_node.data, {'id': 1})
        self.assertEqual(self.ll.tail.next_node, None)
        self.assertEqual(self.ll.tail.data, {'id': 1})

    def test_to_list(self):
        lst = self.ll.to_list()
        self.assertEqual(lst, [])
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = self.ll.to_list()
        self.assertEqual(lst[0], {'id': 0, 'username': 'serebro'})
        self.assertEqual(lst[1], {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(lst[3], {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id(self):
        self.assertEqual(self.ll.get_data_by_id(1), None)
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})
        self.assertEqual(self.ll.get_data_by_id(3), {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id_type_error(self):
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end('idusername')
        self.ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        with self.assertRaises(TypeError):
            self.ll.get_data_by_id(2)
