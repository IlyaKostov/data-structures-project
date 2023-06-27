class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node

        self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """

        if self.head is None:
            return None
        else:
            dequeue_node = self.head
            self.head = self.head.next_node
            return dequeue_node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        queue_list = []
        cur_node = self.head
        while cur_node is not None:
            queue_list.append(cur_node.data)
            cur_node = cur_node.next_node
        queue_list_str = '\n'.join(queue_list)
        return f'{queue_list_str}'
