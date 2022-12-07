import sys
from File import File
from Directory import Directory

MAX_DIR_SIZE_TO_COUNT = 100000
TOTAL_DISK_SPACE = 70000000
REQUIRED_DISK_SPACE = 30000000


def get_directory_sizes_greater_than_or_equal_to_diff(directory: Directory, diff: int):
    big_enough_sizes = []
    size = directory.get_size()
    if size >= diff:
        big_enough_sizes.append(size)

    for child in directory.get_children().values():
        if isinstance(child, Directory):
            big_enough_sizes.extend(get_directory_sizes_greater_than_or_equal_to_diff(child, diff))

    return big_enough_sizes


def get_smallest_size(sizes):
    if len(sizes) == 0:
        return None
    smallest_size = sys.maxsize
    for size in sizes:
        if size < smallest_size:
            smallest_size = size
    return smallest_size


def calculate_answer_part_one(directory: Directory):
    result = 0
    size = directory.get_size()
    if size <= MAX_DIR_SIZE_TO_COUNT:
        result += size

    for child in directory.get_children().values():
        if isinstance(child, Directory):
            result += calculate_answer_part_one(child)

    return result


def build_file_system(data):
    root = Directory("/")
    current_working_directory = root
    for line in data:
        line = line.strip()
        if line.startswith("$"):
            command = line.lstrip("$").split()
            if command[0] == 'cd':
                if command[1] == '..':
                    current_working_directory = current_working_directory.parent
                elif command[1] != '/':
                    current_working_directory = current_working_directory.get_child(command[1])
        else:
            data = line.split()
            if line.startswith("dir"):
                new_directory = Directory(data[1], current_working_directory)
                current_working_directory.add_child(new_directory)
            else:
                new_file = File(data[1], int(data[0]))
                current_working_directory.add_child(new_file)

    return root


def part_one(data):
    file_system = build_file_system(data)
    answer = calculate_answer_part_one(file_system)
    print("The sum of all directories with sizes less than {} is {}".format(MAX_DIR_SIZE_TO_COUNT, answer))


def part_two(data):
    file_system = build_file_system(data)
    used_size = file_system.get_size()
    free_size = (TOTAL_DISK_SPACE - used_size)
    diff = REQUIRED_DISK_SPACE - free_size
    sizes = get_directory_sizes_greater_than_or_equal_to_diff(file_system, diff)
    answer = get_smallest_size(sizes)
    print("The size of the directory we need to delete to make room for the update is {}".format(answer))


def main() -> int:
    with open('../../input/day7') as file:
        data = file.readlines()

    part_one(data)
    part_two(data)

    return 0


if __name__ == '__main__':
    sys.exit(main())
