from typing import Tuple

import pygame as pg

from python.day14.Point import Point
from ScreenAdapter import ScreenAdapter

COLOR = (255, 255, 255)


class Shape:

    def __init__(self, vertices: [Point], screen_adapter: ScreenAdapter):
        self._vertices = vertices
        self._points = [screen_adapter.get_screen_coordinates(v) for v in vertices]
        self._screen_adapter = screen_adapter


    @staticmethod
    def parse(data: str, screen_adapter: ScreenAdapter):
        vertices = []
        pairs = data.split(" -> ")
        for pair in pairs:
            vertices.append(Point.parse(pair))

        return Shape(vertices, screen_adapter)

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

    def draw(self, screen: pg.Surface):
        if len(self._points) > 2:
            pg.draw.polygon(screen, COLOR, self._points, self._screen_adapter.get_scaling_factor())
        else:
            pg.draw.line(screen, COLOR, self._points[0], self._points[1], self._screen_adapter.get_scaling_factor())
