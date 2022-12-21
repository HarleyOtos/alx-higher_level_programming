#!/usr/bin/python3

class Node:
    """
    Node

    This class represents a node in a singly linked list.
    It has a data field and a reference
    to the next node in the list.
    """


    def __init__(self, data, next_node=None):
        """
        Initialize a `Node` instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list. Default is None.

        Raises:
            TypeError: If `data` is not an integer.
            TypeError: If `next_node` is not a `Node` object or None.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: The data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If `value` is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node: The next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list.

        Args:
            value (Node): The new next node in the list.

        Raises:
            TypeError: If `value` is not a `Node` object or None.

        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList

    This class represents a singly linked list. It has a head node that points to the first
    node in the list.

    """
    def __init__(self):
        """
        Initialize a `SinglyLinkedList` instance.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new node with the given value in the list, keeping it sorted in ascending order.

        Args:
            value (int): The value to insert in the list.

        """
        if self.__head is None:
            new = Node(value, None)
            self.__head = new
        else:
            aux = self.__head
            while aux.next_node is not None and value > aux.next_node.data:
                aux = aux.next_node
            if aux.data < value:
                new = Node(value, aux.next_node)
                aux.next_node = new
            else:
                new = Node(value, aux)
                self.__head = new

    def __str__(self):
        """
        Get a string representation of the list.

        Returns:
            str: A string representation of the list, with each node's data on a separate line.

        """
        s = ""
        while self.__head is not None:
            s = s + str(self.__head.data) + "\n"
            self.__head = self.__head.next_node
        return s[:-1]
