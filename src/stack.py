class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        stack_list = []
        cur_node = self.top
        while cur_node is not None:
            stack_list.append(cur_node.data)
            cur_node = cur_node.next_node
        stack_list_str = '\n'.join(stack_list)
        return f'{stack_list_str}'

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next_node = self.top
            self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next_node
            popped_node.next_node = None
            return popped_node.data
