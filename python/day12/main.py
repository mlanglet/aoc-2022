import sys
import time

from python.day12.Node import Node

import pygame as pg

from python.day12.ScreenAdapter import ScreenAdapter

PATH_COLOR = (255, 140, 0)
BACKGROUND_COLOR = (25, 25, 25)
SCALING_FACTOR = 5
WIDTH = 1000
HEIGHT = 400


def build_graph(data: [str]):
    graph = {}
    start = None
    end = None
    for y in range(len(data)):
        row = data[y].strip()
        for x in range(len(row)):
            node = Node(x, y, row[x:x+1])

            if node.is_start():
                start = node
            if node.is_end():
                end = node

            reachable_neighbours = []
            if x > 0:
                neighbour = Node(x-1, y, row[x-1:x])
                if node.can_move_to(neighbour):
                    reachable_neighbours.append(neighbour)
            if x < len(row) - 1:
                neighbour = Node(x+1, y, row[x+1:x+2])
                if node.can_move_to(neighbour):
                    reachable_neighbours.append(neighbour)
            if y > 0:
                neighbour = Node(x, y-1, data[y-1][x:x+1])
                if node.can_move_to(neighbour):
                    reachable_neighbours.append(neighbour)
            if y < len(data) - 2:
                neighbour = Node(x, y+1, data[y+1][x:x+1])
                if node.can_move_to(neighbour):
                    reachable_neighbours.append(neighbour)

            graph[node] = reachable_neighbours

    return graph, start, end


def find_shortest_path(graph, start, end):
    path_list = [[start]]
    path_index = 0
    previous_nodes = {start}
    if start == end:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        if end in next_nodes:
            current_path.append(end)
            return current_path
        for next_node in next_nodes:
            if next_node not in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(next_node)
        path_index += 1
    return []


def part_one(data):
    graph, start, end = build_graph(data)
    shortest_path = find_shortest_path(graph, start, end)

    print("The shortest path to the summit is {} steps.".format(len(shortest_path)-1))

    run_game(graph, shortest_path, start, end)


def part_two(data):
    graph, start, end = build_graph(data)

    best_hike = sys.maxsize
    for key in graph.keys():
        if key.get_type() == 'a':
            shortest_path = find_shortest_path(graph, key, end)
            if len(shortest_path) > 0 and len(shortest_path) - 1 < best_hike:
                best_hike = len(shortest_path) - 1

    print("The best hiking trail to the summit is {} steps.".format(best_hike))


def height_map_color(height) -> tuple[int, int, int]:
    if height < 0:
        return 255, 255, 255
    return ((height/50) * 125), 125 - ((height/75) * 255), 0


def setup():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Day 12 Visualized')
    return screen


def run_game(graph, path, start, end):
    screen = setup()
    adapter = ScreenAdapter(WIDTH, HEIGHT, SCALING_FACTOR)

    clock = pg.time.Clock()
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        clock.tick(60)

        screen.fill(BACKGROUND_COLOR)

        for node in graph:
            pg.draw.rect(screen, height_map_color(node.get_height()), adapter.get_screen_rect(node))

        for node in path:
            pg.draw.rect(screen, PATH_COLOR, adapter.get_screen_rect(node))

        pg.draw.rect(screen, (80, 55, 255), adapter.get_screen_rect(start))
        pg.draw.rect(screen, (80, 255, 255), adapter.get_screen_rect(end))

        pg.display.flip()

    pg.quit()


def main() -> int:
    with open('../../input/day12') as file:
        data = file.readlines()

    start_time = time.time_ns()
    part_two(data)
    print("--- Part two took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    start_time = time.time_ns()
    part_one(data)
    print("--- Part one took %d ms ---" % ((time.time_ns() - start_time) / 1000000))

    return 0


if __name__ == '__main__':
    sys.exit(main())
