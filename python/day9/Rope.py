from Point import Point

INITIAL_X = 0
INITIAL_Y = 0


class Rope:

    def __init__(self, length: int):
        self._knots = []
        for i in range(length):
            self._knots.append(Point(INITIAL_X, INITIAL_Y))

    def __str__(self) -> str:
        string = ""
        for knot in self._knots:
            string += str(knot)
        return string

    def move_rope(self, direction: Point) -> bool:
        """Move the rope in the provided direction
        :param direction: The direction to move the head of the rope
        :type direction: Point

        :returns: True if the tail had to move as a result of the head moving, otherwise False
        :rtype: bool
        """
        self._knots[0] += direction
        for i in range(1, len(self._knots)):
            new_knot_pos = Rope.move_knot(self._knots[i], self._knots[i-1])
            if self._knots[i] == new_knot_pos:
                return False
            self._knots[i] = new_knot_pos

        return True

    @staticmethod
    def move_knot(knot: Point, prev_knot: Point) -> Point:
        if knot.distance(prev_knot) > 1:
            diff = prev_knot - knot
            diff_x = diff.get_x()
            diff_y = diff.get_y()
            if abs(diff.get_x()) > 1:
                diff_x = diff.get_x() / abs(diff.get_x())
            if abs(diff.get_y()) > 1:
                diff_y = diff.get_y() / abs(diff.get_y())

            knot += Point(diff_x, diff_y)
        return knot

    def get_tail(self):
        return self._knots[len(self._knots)-1]
