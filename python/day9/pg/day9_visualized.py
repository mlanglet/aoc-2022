import sys
import pygame as pg
from ScreenAdapter import ScreenAdapter
from Point import Point
from Rope import Rope
from Command import Command

BACKGROUND_COLOR = (25, 25, 25)
WIDTH = 1024
HEIGHT = 768
SCALING_FACTOR = 2


def setup():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Day 9 Visualized')
    return screen


def run_game(data):
    screen = setup()
    screen_adapter = ScreenAdapter(WIDTH, HEIGHT, SCALING_FACTOR)

    command = Command(data)
    rope = Rope(10, screen_adapter)
    points_visited_by_tail = {Point(0, 0)}

    clock = pg.time.Clock()
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        clock.tick(60)

        next_direction = command.get_next_direction()
        tail_moved = rope.move_rope(next_direction)
        if tail_moved:
            points_visited_by_tail.add(rope.get_tail())

        screen.fill(BACKGROUND_COLOR)
        command.draw(screen, points_visited_by_tail)
        rope.draw(screen, points_visited_by_tail)

        pg.display.flip()

    pg.quit()


def main() -> int:
    with open('../../../input/day9') as file:
        data = file.readlines()

    run_game(data)

    return 0


if __name__ == '__main__':
    sys.exit(main())
