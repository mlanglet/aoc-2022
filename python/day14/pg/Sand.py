from Point import Point


class Sand:
    def __init__(self):
        self._pos = Point(500, 0)
        self._is_moving = True

    def __str__(self):
        return self._pos.__str__()

    def stop(self) -> None:
        self._is_moving = False

    def is_moving(self) -> bool:
        return self._is_moving

    def get_pos(self) -> Point:
        return self._pos

    def get_next_pos(self) -> Point:
        return Point(self._pos.get_x(), self._pos.get_y() + 1)

    def set_next_pos(self, new_pos: Point) -> None:
        self._pos = new_pos

    def is_falling_into_the_abyss(self) -> bool:
        return self._pos.get_y() > 500
