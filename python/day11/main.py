import sys
import time
from MonkeyParser import MonkeyParser


def play_rounds(data, worry_level_modifier, rounds):
    monkeys = MonkeyParser.parse_monkeys(data, worry_level_modifier)

    for _ in range(0, rounds):
        for monkey in monkeys:
            for action in monkey.do_turn():
                monkeys[action[0]].catch_item(action[1])

    top1, top2 = 0, 0
    for monkey in monkeys:
        inspections = monkey.get_inspections()
        if inspections > top1:
            top2 = top1
            top1 = inspections
        elif inspections > top2:
            top2 = inspections

    print("The level of monkey business is %d" % (top1 * top2))


def part_one(data):
    worry_level_modifier = lambda x: x // 3
    play_rounds(data, worry_level_modifier, 20)


def part_two(data):
    play_rounds(data, None, 10000)


def main() -> int:
    with open('../../input/day11') as file:
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
