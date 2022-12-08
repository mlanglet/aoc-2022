
class Tree:
    def __init__(self, x: int, y: int, h: int):
        self._x = x
        self._y = y
        self._h = h

    def __str__(self):
        return "x: {} y: {} h: {}".format(self._x, self._y, self._h)

    def __eq__(self, other):
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_height(self):
        return self._h
