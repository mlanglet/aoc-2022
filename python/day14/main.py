import sys
import time
from typing import Dict

from Shape import Shape
from python.day14.Point import Point
from python.day14.Sand import Sand


def run_simulation(solid_area: Dict[Point, bool]) -> int:
    sand_pile = []
    falling_grain = Sand()

    while True:
        next_pos = falling_grain.get_next_pos()
        if is_point_blocked(next_pos, solid_area):
            left = next_pos + Point(-1, 0)
            if is_point_blocked(left, solid_area):
                right = next_pos + Point(1, 0)
                if is_point_blocked(right, solid_area):
                    falling_grain.stop()
                else:
                    next_pos = right
            else:
                next_pos = left

        if falling_grain.is_moving():
            falling_grain.set_next_pos(next_pos)
        else:
            solid_area[falling_grain.get_pos()] = True
            sand_pile.append(falling_grain)
            if falling_grain.is_blocking_new_sand():
                return len(sand_pile)

            falling_grain = Sand()

        if falling_grain.is_falling_into_the_abyss():
            return len(sand_pile)


def is_point_blocked(next_pos: Point, solid: Dict[Point, bool]):
    return solid.get(next_pos, False)


def part_one(data):
    solid_area = {}
    for line in data:
        shape = Shape.parse(line.strip())
        for point in shape.get_solid_area():
            solid_area[point] = True

    answer = run_simulation(solid_area)

    print('The amount of sand that fell before it spilled out was {}'.format(answer))


def part_two(data):
    solid_area = {}
    max_y = 0
    for line in data:
        shape = Shape.parse(line.strip())
        for point in shape.get_solid_area():
            solid_area[point] = True
            if point.get_y() > max_y:
                max_y = point.get_y()

    floor = Shape([Point(-1000, max_y + 2), Point(2000, max_y + 2)])
    for tile in floor.get_solid_area():
        solid_area[tile] = True

    answer = run_simulation(solid_area)

    print('The amount of sand that fell before it blocked new sand from coming in was {}'.format(answer))


def main() -> int:
    with open('../../input/day14') as file:
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
