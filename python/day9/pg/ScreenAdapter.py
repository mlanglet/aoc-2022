from pygame.rect import Rect
from Point import Point


class ScreenAdapter:

    def __init__(self, width: int, height: int, scaling_factor: int):
        self._width = width
        self._height = height
        self._scaling_factor = scaling_factor

    def get_screen_coordinates(self, point: Point) -> Point:
        return Point((point.get_x() * self._scaling_factor) + 100,  # Offset keeps the rope on the screen
                     (point.get_y() * self._scaling_factor) + self._height // 2)

    def get_scaled_rect(self, point: Point) -> Rect:
        return Rect(point.get_x(), point.get_y(), self._scaling_factor, self._scaling_factor)
