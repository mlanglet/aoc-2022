from typing import Set

import pygame as pg
from Point import Point


TEXT_COLOR = (255, 255, 255)
STILL = Point(0, 0)
UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)


class Command:
    def __init__(self, data: [str]):
        self._data = data

        self._current_direction = STILL
        self._current_step = 0
        self._current_steps = 0
        self._command_counter = 0

        pg.init()
        self._font = pg.font.Font('freesansbold.ttf', 16)

    def get_next_direction(self):
        if self._command_counter >= len(self._data):
            return STILL

        if self._current_step == self._current_steps:
            command = self._data[self._command_counter]
            self._current_steps = int(command[2:len(command)])
            self._current_step = 1

            heading = command[0:1]
            if heading == 'U':
                self._current_direction = UP
            elif heading == 'D':
                self._current_direction = DOWN
            elif heading == 'L':
                self._current_direction = LEFT
            elif heading == 'R':
                self._current_direction = RIGHT
            else:
                self._current_direction = STILL
            self._command_counter += 1
        else:
            self._current_step += 1

        return self._current_direction

    def draw(self, screen: pg.Surface, history: Set[Point]):
        move_counter_text = self._font.render("Move: {}".format(self._command_counter), True, TEXT_COLOR)
        points_counter_text = self._font.render("Points visited by tail: {}".format(len(history)), True, TEXT_COLOR)

        move_counter_text_rect = move_counter_text.get_rect()
        move_counter_text_rect.x = 25
        move_counter_text_rect.y = 25
        points_counter_text_rect = points_counter_text.get_rect()
        points_counter_text_rect.x = 25
        points_counter_text_rect.y = 52

        screen.blit(move_counter_text, move_counter_text_rect)
        screen.blit(points_counter_text, points_counter_text_rect)
