import math


class Node:

    def __init__(self, x: int, y: int, h: str) -> None:
        self._x = x
        self._y = y
        self._type = h

        if h == 'S':
            self._h = ord('a') - 96
        elif h == 'E':
            self._h = ord('z') - 96
        else:
            self._h = ord(h) - 96

    def __str__(self) -> str:
        return "({}, {} @ {})".format(self._x, self._y, self._h)

    def __eq__(self, other):
        return self._x == other.get_x() and self._y == other.get_y()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._x) ^ hash(self._y)

    def __add__(self, other):
        return Node(self._x + other.get_x(), self._y + other.get_y())

    def __sub__(self, other):
        return Node(self._x - other.get_x(), self._y - other.get_y())

    def is_start(self):
        return self._type == "S"

    def is_end(self):
        return self._type == "E"

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_height(self):
        return self._h

    def get_type(self):
        return self._type

    def can_move_to(self, other):
        return self._h + 1 >= other.get_height()

    def distance(self, other) -> int:
        return int(math.sqrt((other.get_x() - self.get_x()) ** 2 + (other.get_y() - self.get_y()) ** 2))
