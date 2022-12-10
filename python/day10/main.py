import sys
import time


def part_one(program):
    measuring_cycles = {20, 60, 100, 140, 180, 220}
    signal_strength_sum = 0
    x = 1
    adds = {}
    busy = 0
    instruction_counter = 0
    for cycle_count in range(0, 240):
        if busy == 0:
            instruction = program[instruction_counter]
            if instruction[0:4] == "noop":
                busy = 1
            if instruction[0:4] == "addx":
                busy = 2
                adds[cycle_count+2] = int(instruction[5:len(instruction)])
            instruction_counter += 1

        if cycle_count in measuring_cycles:
            signal_strength_sum += x * cycle_count

        if adds.get(cycle_count):
            y = adds.pop(cycle_count)
            x += y

        busy -= 1

    print("The sum of signal strength measured at cycles {} is {}".format(measuring_cycles, signal_strength_sum))


def print_screen(pixels: [[str]]):
    for row in pixels:
        line = ""
        for pixel in row:
            line += pixel
        print(line)


def draw_pixel(x: int, col: int):
    if x-1 <= col <= x+1:
        return "#"
    return "."


def part_two(program):
    line_breaks = {39, 79, 119, 159, 199, 239}
    pixels = [[], [], [], [], [], []]
    row = 0
    column = 0
    x = 1
    adds = {}
    busy = 0
    instruction_counter = 0
    for cycle_count in range(0, 240):
        if busy == 0:
            instruction = program[instruction_counter]
            if instruction[0:4] == "noop":
                busy = 1
            if instruction[0:4] == "addx":
                busy = 2
                adds[cycle_count+1] = int(instruction[5:len(instruction)])
            instruction_counter += 1

        pixels[row].append(draw_pixel(x, column))

        if adds.get(cycle_count):
            y = adds.pop(cycle_count)
            x += y

        busy -= 1

        if column in line_breaks:
            row += 1
            column = 0
        else:
            column += 1

    print_screen(pixels)


def main() -> int:
    with open('../../input/day10') as file:
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
