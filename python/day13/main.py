import sys
import time
from functools import reduce
from operator import add


def is_ordered(value1, value2):
    if type(value1) == type(int) and type(value2) == type(int):
        if value1 > value2:
            return False
        return True

    if isinstance(value1, list) and isinstance(value2, int):
        value2 = [value2]

    if isinstance(value1, int) and isinstance(value2, list):
        value1 = [value1]

    for i in range(len(value1)):
        if i == len(value2):
            return False
        if value1[i] > value2[i]:
            return False

    return True


def convert_value(line: str):
    count_of_open_square_brackets = line.count("[")
    index = line.find("[")
    if count_of_open_square_brackets > 1:
        line = line[0:index+1] + line[index+1:len(line)].replace("[", "")

    count_of_closed_square_brackets = line.count("]")
    index = line.rfind("]")
    if count_of_closed_square_brackets > 1:
        line = line[0:index].replace("]", "") + line[index:len(line)]

    while line.find(",,") > -1:
        line = line.replace(",,", ",")

    while line.find("[,") > -1:
        line = line.replace("[,", "[")

    return line


def part_one(data):
    packet1 = None
    packet2 = None
    ordered_pair_indexes = []
    index = 1

    for line in data:
        if line == '\n':
            if is_ordered(packet1, packet2):
                print('packets \n{}\n{}\nare ordered!'.format(packet1, packet2))
                ordered_pair_indexes.append(index)
            packet1 = None
            packet2 = None
            index += 1
            continue

        line = line.strip()
        if packet1 is None:
            packet1 = eval(line)
        else:
            packet2 = eval(line)

    answer = reduce(add, ordered_pair_indexes)

    print(ordered_pair_indexes)

    print('{} sum of indexes of pairs that are in order'.format(answer))


def part_two(data):
    print('Part two!')


def main() -> int:
    with open('../../input/day13') as file:
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
