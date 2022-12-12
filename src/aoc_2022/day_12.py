import heapq
import logging
import sys
from collections import defaultdict

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_shortest_path(positions: list[tuple[int, int]],
                     edges: dict[tuple[int, int], tuple[int, int]],
                     start_positions: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    # Dijkstra's algorithm
    visited: set[tuple[int, int]] = set()
    shortest_path: dict[tuple[int, int], int] = {}
    max_value = sys.maxsize
    for node in positions:
        shortest_path[node] = max_value
    for start_position in start_positions:
        shortest_path[start_position] = 0

    priority_queue: list[tuple[int, tuple[int, int]]] = []
    for start_position in start_positions:
        heapq.heappush(priority_queue, (0, start_position))

    while not len(priority_queue) == 0:
        distance, current_position = heapq.heappop(priority_queue)
        visited.add(current_position)

        neighbors = edges[current_position]
        for neighbor in neighbors:
            if neighbor not in visited:
                distance = edges[current_position][neighbor]
                if neighbor not in visited:
                    old_cost: int = shortest_path[neighbor]
                    new_cost: int = shortest_path[current_position] + distance
                    if new_cost < old_cost:
                        priority_queue.append((new_cost, neighbor))
                        shortest_path[neighbor] = new_cost


    return shortest_path

def generate_heightmap(heightmap_input: list[str]) -> tuple[
        dict[int, list[int]], list[tuple[int, int]], tuple[int, int], tuple[int, int]]:
    heightmap = defaultdict(list)
    positions = []
    current_position = (0, 0)
    end_position = (0, 0)
    for y, line in enumerate(heightmap_input):
        for x, height_string in enumerate(line):
            if height_string == 'S':
                height = 0
                current_position = (x, y)
            elif height_string == 'E':
                height = 27
                end_position = (x, y)
            else:
                height = ord(height_string) - ord('a') + 1
            heightmap[y].append(height)
            positions.append((x, y))

    return heightmap, positions, current_position, end_position


def get_edges(heightmap: dict[int, list[int]]) -> dict[tuple[int, int], tuple[int, int]]:
    edges = defaultdict(dict)
    for y, lines in heightmap.items():
        for x, height in enumerate(lines):
            down = heightmap[y + 1][x] if y + 1 < len(heightmap) else None
            if down is not None:
                down_distance = down - height
                if down_distance <= 1:
                    edges[(x, y)][(x, y + 1)] = 1

            right = heightmap[y][x + 1] if x + 1 < len(lines) else None
            if right is not None:
                right_distance = right - height
                if right_distance <= 1:
                    edges[(x, y)][(x + 1, y)] = 1

            up = heightmap[y - 1][x] if y - 1 >= 0 else None
            if up is not None:
                up_distance = up - height
                if up_distance <= 1:
                    edges[(x, y)][(x, y - 1)] = 1

            left = heightmap[y][x - 1] if x - 1 >= 0 else None
            if left is not None:
                left_distance = left - height
                if left_distance <= 1:
                    edges[(x, y)][(x - 1, y)] = 1

    return edges

def print_path(heightmap: dict[int, list[int]], shortest_path: dict[tuple[int, int], int]):
    if logger.level != logging.DEBUG:
        return

    logger.debug('')
    for y in range(len(heightmap)):
        line = ''
        for x in range(len(heightmap[y])):
            cost = shortest_path[(x, y)]
            if cost == sys.maxsize:
                cost = -1
            line += f'{cost:4}'
        logger.debug(line)

def get_fewest_steps_from_start_position(heightmap_input: list[str]) -> int:
    heightmap, positions, current_position, end_position = generate_heightmap(heightmap_input)
    edges = get_edges(heightmap)
    shortest_path = get_shortest_path(positions, edges, [current_position])
    print_path(heightmap, shortest_path)
    return shortest_path[end_position]

def get_fewest_steps_from_all_start_positions(heightmap_input: list[str]) -> int:
    heightmap, positions, current_position, end_position = generate_heightmap(heightmap_input)
    start_positions: list[tuple[int, int]] = []
    for position in positions:
        if heightmap[position[1]][position[0]] == 0 or heightmap[position[1]][position[0]] == 1:
            start_positions.append(position)

    edges = get_edges(heightmap)
    shortest_path = get_shortest_path(positions, edges, start_positions)
    print_path(heightmap, shortest_path)
    return shortest_path[end_position]
