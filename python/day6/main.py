import sys


def find_unique_sequence(length, data):
    for i in range(len(data)):
        if len(set(data[i:i + length])) == length:
            return i + length

    return -1


def search_and_report(sequence_length, data):
    res = find_unique_sequence(sequence_length, data)
    if res == -1:
        print('Unique sequence of length {} not found in data'.format(sequence_length))
    else:
        print('First packet marker is found after {} characters'.format(res))


def part_one(data):
    search_and_report(4, data)


def part_two(data):
    search_and_report(14, data)


def main() -> int:
    with open('../../input/day6') as file:
        data = file.read(4094)

    part_one(data)
    part_two(data)

    return 0


if __name__ == '__main__':
    sys.exit(main())
