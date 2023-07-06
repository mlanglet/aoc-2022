from typing import Tuple

from Point import Point

class Shape:

    def __init__(self, vertices: [Point]):
        self._vertices = vertices

    @staticmethod
    def parse(data: str):
        vertices = []
        pairs = data.split(" -> ")
        for pair in pairs:
            vertices.append(Point.parse(pair))

        return Shape(vertices)

    def get_solid_area(self) -> [Tuple[int, int]]:
        solid_area = []
        for i in range(1, len(self._vertices)):
            previous = self._vertices[i - 1]
            current = self._vertices[i]

            solid_area.append(previous)
            solid_area.append(current)

            is_vertical_line = current.get_x() == previous.get_x()
            if is_vertical_line:
                if previous.get_y() < current.get_y():
                    modifier = Point(0, 1)
                else:
                    modifier = Point(0, -1)
            else:
                if previous.get_x() < current.get_x():
                    modifier = Point(1, 0)
                else:
                    modifier = Point(-1, 0)

            distance = current.distance(previous)
            if distance > 0:
                for j in range(0, distance):
                    new_solid = previous + modifier



                    solid_area.append(new_solid)
                    previous = new_solid

        return solid_area
