import sys
import time
from functools import reduce, cmp_to_key
from operator import add


def compare(left, right) -> int:
    if type(left) == int and type(right) == int:
        return left - right

    if type(left) == list and type(right) == list:
        if len(left) == 0:
            if len(right) == 0:
                return 0
            else:
                return -1

        min_size = min(len(left), len(right))
        for i in range(min_size):
            check = compare(left[i], right[i])
            if check != 0:
                return check

        return len(left) - len(right)

    if type(left) == int:
        return compare([left], right)

    return compare(left, [right])


def part_one(data):
    left = None
    right = None
    ordered_pair_indexes = []
    index = 1

    for line in data:
        if line == '\n':
            if compare(left, right) <= 0:
                ordered_pair_indexes.append(index)
            left = None
            right = None
            index += 1
            continue

        line = line.strip()
        if left is None:
            left = eval(line)
        else:
            right = eval(line)

    answer = reduce(add, ordered_pair_indexes)

    print('{} sum of indexes of pairs that are in order'.format(answer))


def part_two(data):
    packets = [[2], [6]]
    for line in data:
        if line == '\n':
            continue
        packets.append(eval(line))

    sorted_packets = sorted(packets, key=cmp_to_key(compare))

    print('The product of indexes of the divider packets is {}'
          .format((sorted_packets.index([2]) + 1) * (sorted_packets.index([6]) + 1)))


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
