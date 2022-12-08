import sys
import time
from Tree import Tree


def build_forest(data) -> [[Tree]]:
    forest = []
    y = 0
    for line in data:
        line = line.rstrip()
        row = []
        for x in range(len(line)):
            h = int(line[x:x + 1])
            row.append(Tree(x, y, h))
        forest.append(row)
        y += 1
    return forest


def is_tree_visible(tree: Tree, forest: [[]]) -> bool:
    if is_visible_from_west(tree, forest):
        return True
    if is_visible_from_north(tree, forest):
        return True
    if is_visible_from_east(tree, forest):
        return True
    if is_visible_from_south(tree, forest):
        return True
    return False


def is_visible_from_west(tree: Tree, forest, dx=None) -> bool:
    if tree.get_x() == 0:
        return True

    if dx is None:
        dx = tree.get_x()

    dx -= 1

    if tree.get_height() <= forest[tree.get_y()][dx].get_height():
        return False

    if dx == 0:
        return True

    return is_visible_from_west(tree, forest, dx)


def is_visible_from_north(tree: Tree, forest, dy=None) -> bool:
    if tree.get_y() == 0:
        return True

    if dy is None:
        dy = tree.get_y()

    dy -= 1

    if tree.get_height() <= forest[dy][tree.get_x()].get_height():
        return False

    if dy == 0:
        return True

    return is_visible_from_north(tree, forest, dy)


def is_visible_from_east(tree: Tree, forest, dx=None) -> bool:
    grid_size = len(forest) - 1
    if tree.get_x() == grid_size:
        return True

    if dx is None:
        dx = tree.get_x()

    dx += 1

    if tree.get_height() <= forest[tree.get_y()][dx].get_height():
        return False

    if dx == grid_size:
        return True

    return is_visible_from_east(tree, forest, dx)


def is_visible_from_south(tree: Tree, forest, dy=None) -> bool:
    grid_size = len(forest) - 1
    if tree.get_y() == grid_size:
        return True

    if dy is None:
        dy = tree.get_y()

    dy += 1

    if tree.get_height() <= forest[dy][tree.get_x()].get_height():
        return False

    if dy == grid_size:
        return True

    return is_visible_from_south(tree, forest, dy)


def part_one(forest) -> None:
    visible_trees = 0
    for x in range(len(forest)):
        for y in range(len(forest[0])):
            tree = forest[x][y]
            if is_tree_visible(tree, forest):
                visible_trees += 1

    print("{} trees are visible.".format(visible_trees))


def calculate_scenic_score(tree: Tree, forest: [[]]) -> int:
    view_distance_west = find_view_distance_west(tree, forest)
    view_distance_north = find_view_distance_north(tree, forest)
    view_distance_east = find_view_distance_east(tree, forest)
    view_distance_south = find_view_distance_south(tree, forest)
    return view_distance_west * view_distance_north * view_distance_east * view_distance_south


def find_view_distance_west(tree: Tree, forest, dx=None, view_distance=1) -> int:
    if tree.get_x() == 0:
        return view_distance

    if dx is None:
        dx = tree.get_x()

    dx -= 1

    if tree.get_height() <= forest[tree.get_y()][dx].get_height():
        return view_distance

    if dx == 0:
        return view_distance

    view_distance += 1

    return find_view_distance_west(tree, forest, dx, view_distance)


def find_view_distance_north(tree: Tree, forest, dy=None, view_distance=1) -> int:
    if tree.get_y() == 0:
        return view_distance

    if dy is None:
        dy = tree.get_y()

    dy -= 1

    if tree.get_height() <= forest[dy][tree.get_x()].get_height():
        return view_distance

    if dy == 0:
        return view_distance

    view_distance += 1

    return find_view_distance_north(tree, forest, dy, view_distance)


def find_view_distance_east(tree: Tree, forest, dx=None, view_distance=1) -> int:
    grid_size = len(forest) - 1
    if tree.get_x() == grid_size:
        return view_distance

    if dx is None:
        dx = tree.get_x()

    dx += 1

    if tree.get_height() <= forest[tree.get_y()][dx].get_height():
        return view_distance

    if dx == grid_size:
        return view_distance

    view_distance += 1

    return find_view_distance_east(tree, forest, dx, view_distance)


def find_view_distance_south(tree: Tree, forest, dy=None, view_distance=1) -> int:
    grid_size = len(forest) - 1
    if tree.get_y() == grid_size:
        return view_distance

    if dy is None:
        dy = tree.get_y()

    dy += 1

    if tree.get_height() <= forest[dy][tree.get_x()].get_height():
        return view_distance

    if dy == grid_size:
        return view_distance

    view_distance += 1

    return find_view_distance_south(tree, forest, dy, view_distance)


def part_two(forest) -> None:
    high_score = 0
    for x in range(len(forest)):
        for y in range(len(forest[0])):
            score = calculate_scenic_score(forest[x][y], forest)
            if score > high_score:
                high_score = score

    print("The highest scenic score in the forest is {}.".format(high_score))


def main() -> int:
    start_time = time.time_ns()
    with open('../../input/day8') as file:
        data = file.readlines()
    forest = build_forest(data)
    print("--- Building the forest took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    start_time = time.time_ns()
    part_one(forest)
    print("--- Part one took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    start_time = time.time_ns()
    part_two(forest)
    print("--- Part two took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    return 0


if __name__ == '__main__':
    sys.exit(main())
