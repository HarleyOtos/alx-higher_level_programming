#!/usr/bin/python3
"""Square Class
This module contains the `Square` class and its methods.
"""


class Square:
    """Square Class
    This class represents a square with a size and a position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square instance.

        Args:
            size (int, optional): The size of the square. Default is 0.
            position (tuple, optional): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
            TypeError: If `position` is not a tuple of 2 positive integers.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        if self.__check_tuple(position) is False \
            or self.__check_indexes(position) is False \
            or self.__check_integers(position) is False \
            or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.size = size
        self.position = position

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def position(self):
        """tuple: The position of the square."""
        return self.__position

    @position.setter
    def position(self, position):
        """Set the position of the square.

        Args:
            position (tuple): The new position of the square.

        Raises:
            TypeError: If `position` is not a tuple of 2 positive integers.

        """
        if self.__check_tuple(position) is False \
            or self.__check_indexes(position) is False \
            or self.__check_integers(position) is False \
            or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_tuple(self, position):
        """Check if `position` is a tuple.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if `position` is a tuple, False otherwise.

        """
        if type(position) is tuple:
            return True

        return False

    def __check_indexes(self, position):
        """Check if `position` has 2 elements.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if `position` has 2 elements, False otherwise.

        """
        if len(position) == 2:
            return True

        return False

    def __check_integers(self, position):
        """Check if the elements of `position` are integers.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if the elements of `position` are integers, False otherwise.

        """
        if type(position[0]) is int and type(position[1]) is int:
            return True

        return False

    def __check_values(self, position):
        """Check if the elements of `position` are positive.

        Args:
            position (tuple): The position to check.

        Returns:
            bool: True if the elements of `position` are positive, False otherwise.

        """
        if position[0] >= 0 and position[1] >= 0:
            return True

        return False

    def area(self):
        """Get the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the `#` character.

        If the size is 0, print an empty line.

        """
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
