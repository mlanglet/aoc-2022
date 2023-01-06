import sys
import time
from typing import Dict

import pygame as pg

from Shape import Shape
from Point import Point
from Sand import Sand
from ScreenAdapter import ScreenAdapter

BACKGROUND_COLOR = (25, 25, 25)
SAND_COLOR = (255, 255, 0)
FALLING_SAND_COLOR = (255, 0, 0)
WIDTH = 800
HEIGHT = 600
SCALING_FACTOR = 1


def setup():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Day 14 Visualized')
    return screen


def run_game(shapes: [Shape], solid_area: Dict[Point, bool], screen_adapter: ScreenAdapter) -> int:
    screen = setup()

    sand_pile = []
    clock = pg.time.Clock()
    sand = Sand()

    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        clock.tick(60)

        next_pos = sand.get_next_pos()
        if is_point_blocked(next_pos, solid_area):
            left = next_pos + Point(-1, 0)
            if is_point_blocked(left, solid_area):
                right = next_pos + Point(1, 0)
                if is_point_blocked(right, solid_area):
                    sand.stop()
                else:
                    next_pos = right
            else:
                next_pos = left

        if sand.is_moving():
            sand.set_next_pos(next_pos)
        else:
            solid_area[sand.get_pos()] = True
            sand_pile.append(sand)
            sand = Sand()

        if sand.is_falling_into_the_abyss():
            running = False
            continue

        screen.fill(BACKGROUND_COLOR)

        pg.draw.rect(screen, FALLING_SAND_COLOR, screen_adapter.get_scaled_rect(sand.get_pos()))

        for grain in sand_pile:
            pg.draw.rect(screen, SAND_COLOR, screen_adapter.get_scaled_rect(grain.get_pos()))

        for shape in shapes:
            shape.draw(screen)

        pg.display.flip()

    pg.quit()

    return len(sand_pile)


def is_point_blocked(next_pos: Point, solid: Dict[Point, bool]):
    return solid.get(next_pos, False)


def part_one(data):
    shapes = []
    solid_area = {}
    screen_adapter = ScreenAdapter(WIDTH, HEIGHT, SCALING_FACTOR)
    for line in data:
        shape = Shape.parse(line.strip(), screen_adapter)
        shapes.append(shape)
        for point in shape.get_solid_area():
            solid_area[point] = True

    answer = run_game(shapes, solid_area, screen_adapter)

    print('The amount of sand that fell before it spilled out was {}'.format(answer))


def part_two(data):
    answer = 'part two!'

    print('{}'.format(answer))


def main() -> int:
    with open('../../../input/day14') as file:
        data = file.readlines()

    start_time = time.time_ns()
    part_one(data)
    print("--- Part one took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    start_time = time.time_ns()
    part_two(data)
    print("--- Part two took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    return 0


if __name__ == '__main__':
    sys.exit(main())
