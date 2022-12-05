def load_stacks(file):
    #         1   2   3   4   5   6   7   8   9
    stacks = [[], [], [], [], [], [], [], [], []]
    for i in range(8):
        row = file.readline()
        for x in range(len(stacks)):
            crate = row[1:2]
            row = row[4:len(row)]
            if crate != ' ' and crate != '':
                stacks[x].insert(0, crate)
    return stacks


def skip_two_lines(file):
    file.readline()
    file.readline()


def print_stacks(stacks):
    tallest_stack = 0
    for i in range(len(stacks)):
        if len(stacks[i]) > tallest_stack:
            tallest_stack = len(stacks[i])

    for i in range(tallest_stack, -1, -1):
        row = ""
        for x in range(len(stacks)):
            if len(stacks[x]) > i:
                row = row + "[{}] ".format(stacks[x][i])
            else:
                row = row + "    "

        print(row)
    print(" 1   2   3   4   5   6   7   8   9")


def part_one():
    with open('../../input/day5') as file:
        stacks = load_stacks(file)

        skip_two_lines(file)

        print_stacks(stacks)

        for move in file:
            tokens = move.split()
            number = int(tokens[1])
            from_stack = int(tokens[3]) - 1
            to_stack = int(tokens[5]) - 1
            for i in range(number):
                stacks[to_stack].append(stacks[from_stack].pop())

        print_stacks(stacks)

        answer = ""
        for i in range(len(stacks)):
            answer = answer + stacks[i].pop()

        print("Using CrateMover 9000, the elves can expect the arrangement {}".format(answer))


def part_two():
    with open('../../input/day5') as file:
        stacks = load_stacks(file)

        skip_two_lines(file)

        for move in file:
            tokens = move.split()
            number = int(tokens[1])
            from_stack = int(tokens[3]) - 1
            to_stack = int(tokens[5]) - 1
            stack_to_be_moved = []
            for i in range(number):
                stack_to_be_moved.insert(0, stacks[from_stack].pop())

            stacks[to_stack].extend(stack_to_be_moved)

        print_stacks(stacks)

        answer = ""
        for i in range(len(stacks)):
            answer = answer + stacks[i].pop()

        print("Using CrateMover 9001, the elves can expect the arrangement {}".format(answer))


part_one()
part_two()
