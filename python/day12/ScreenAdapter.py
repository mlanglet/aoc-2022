from pygame.rect import Rect
from Node import Node


class ScreenAdapter:

    def __init__(self, width: int, height: int, scaling_factor: int):
        self._width = width
        self._height = height
        self._scaling_factor = scaling_factor

    def get_screen_rect(self, point: Node) -> Rect:
        return Rect((point.get_x() * self._scaling_factor) + 6,
                    (point.get_y() * self._scaling_factor) + 6,
                    self._scaling_factor,
                    self._scaling_factor)
