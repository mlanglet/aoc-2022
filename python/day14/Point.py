import math


class Point:

    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return "({}, {})".format(self._x, self._y)

    def __eq__(self, other):
        return self._x == other.get_x() and self._y == other.get_y()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self._x) ^ hash(self._y)

    def __add__(self, other):
        return Point(self._x + other.get_x(), self._y + other.get_y())

    def __sub__(self, other):
        return Point(self._x - other.get_x(), self._y - other.get_y())

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def distance(self, other) -> int:
        return int(math.sqrt((other.get_x() - self.get_x()) ** 2 + (other.get_y() - self.get_y()) ** 2))

    @staticmethod
    def parse(data: str):
        pair = data.split(",")
        return Point(int(pair[0]), int(pair[1]))