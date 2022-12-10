import sys
import time
from Point import Point
from Rope import Rope

UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)


def apply_moves(data: [str], length: int):
    points_visited_by_tail = set()
    points_visited_by_tail.add(Point(0, 0))
    rope = Rope(length)
    for move in data:
        direction = move[0:1]
        if direction == 'U':
            direction = UP
        elif direction == 'D':
            direction = DOWN
        elif direction == 'L':
            direction = LEFT
        elif direction == 'R':
            direction = RIGHT
        else:
            continue

        steps = int(move[2:len(move)])
        for i in range(steps):
            tail_moved = rope.move_rope(direction)
            if tail_moved:
                points_visited_by_tail.add(rope.get_tail())

    print("{} points are visited by the tail".format(len(points_visited_by_tail)))


def part_one(data):
    apply_moves(data, 2)


def part_two(data):
    apply_moves(data, 10)


def main() -> int:
    with open('../../input/day9') as file:
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
