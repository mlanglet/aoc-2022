import math

from Monkey import Monkey
from typing import Callable


class MonkeyParser:

    @staticmethod
    def parse_monkeys(data: [str], worry_level_modifier: Callable[[int], int]) -> [Monkey]:

        if worry_level_modifier is None:
            divisors = []
            for line in data:
                line = line.strip()
                if line.startswith("T"):
                    words = line.split(" ")
                    divisors.append(int(words[len(words) - 1]))

            least_common_multiplier = math.lcm(*divisors)
            worry_level_modifier = lambda x, lcm=least_common_multiplier: x % lcm

        add = lambda x, y: x + y
        mult = lambda x, y: x * y
        square = lambda x: x * x
        monkeys = []
        items = None
        operation = None
        test = None
        divisor = None

        true_target = None
        for line in data:
            if line.startswith('Monkey'):
                continue
            if line == '\n':
                monkeys.append(Monkey(items, operation, worry_level_modifier, test))
                continue
            line = line.strip()
            if line.startswith("S"):
                items = [int(x) for x in (line.split(":")[1].split(","))]
                continue
            if line.startswith("O"):
                words = line.split(" ")
                if words[5] == 'old':
                    operation = square
                elif words[4] == '+':
                    operator = int(words[5])
                    operation = lambda x, y=operator: add(x, y)
                elif words[4] == '*':
                    operator = int(words[5])
                    operation = lambda x, y=operator: mult(x, y)
                continue
            if line.startswith("T"):
                words = line.split(" ")
                divisor = int(words[len(words)-1])
                continue
            if line.startswith("If true"):
                words = line.split(" ")
                true_target = int(words[len(words)-1])
                continue
            if line.startswith("If false"):
                words = line.split(" ")
                false_target = int(words[len(words)-1])
                test = (lambda x, tt=true_target, d=divisor, ft=false_target: (tt, x) if x % d == 0 else (ft, x))
        return monkeys
