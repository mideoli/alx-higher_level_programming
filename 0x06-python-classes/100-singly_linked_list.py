#!/usr/bin/python3
"""File: 100-singly_linked_list.py
Author: Miguel
"""


class Node:
    """Represents a node of a singly linked list.
    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): Reference to the next node\
                    in the list (default is None).
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Retrieve the data stored in the node."""
            return self.__data

        @data.setter
        def data(self, value):
            """Set the data stored in the node.
            Args:
                value (int): The data value to be stored.
            Raises:
                TypeError: If the value is not an integer.
            """
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Retrieve the reference to the next node."""
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """
            Set the reference to the next node.

            Args:
                value (Node): The next node to be referenced.

            Raises:
                TypeError: If the value is not a Node object.
            """
            if value is not None and not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new node with the given value in the sorted order.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
