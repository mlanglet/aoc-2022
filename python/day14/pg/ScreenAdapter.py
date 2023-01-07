from typing import Tuple

from pygame.rect import Rect
from python.day14.Point import Point


class ScreenAdapter:

    def __init__(self, width: int, height: int, scaling_factor: int):
        self._width = width
        self._height = height
        self._scaling_factor = scaling_factor

    def get_scaling_factor(self) -> int:
        return self._scaling_factor

    def get_screen_coordinates(self, point: Point) -> Tuple[int, int]:
        return \
            ((point.get_x() * self._scaling_factor) + self._width // 2) - 500, \
            (point.get_y() * self._scaling_factor) + self._height // 2 - 200

    def get_scaled_rect(self, point: Point) -> Rect:
        screen_coordinates = self.get_screen_coordinates(point)
        return Rect(screen_coordinates[0], screen_coordinates[1], self._scaling_factor, self._scaling_factor)
