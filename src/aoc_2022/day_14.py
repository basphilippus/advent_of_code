import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


ORIGIN = '+'
SAND = 'o'
WALL = '#'
EMPTY = '.'

def print_cave(cave: dict[tuple[int, int], str]):
    if not logger.isEnabledFor(logging.DEBUG):
        return

    min_x = min([x for x, _ in cave.keys()])
    max_x = max([x for x, _ in cave.keys()])
    min_y = min([y for _, y in cave.keys()])
    max_y = max([y for _, y in cave.keys()])

    logger.debug('')

    min_x_string = str(min_x)
    max_x_string = str(max_x)
    origin_string = str(500)
    before_origin_range = 500 - min_x
    after_origin_range = max_x - 500 - 1
    for i in range(0, len(min_x_string)):
        logger.debug(f'{" " * 3}'
              f'{min_x_string[i]}'
              f'{" " * before_origin_range}'
              f'{origin_string[i]}'
              f'{" " * after_origin_range}'
              f'{max_x_string[i]}')

    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x - 1, max_x + 1):
            if x == min_x - 1:
                line += f'{str(y).ljust(3)}'
            line += cave.get((x, y), EMPTY)
        logger.debug(line)
    pass

def count_sand(traces: list[str], floor: bool = False) -> int:
    cave: dict[tuple[int, int], str] = {}
    sand_origin = (500, 0)
    cave[sand_origin] = ORIGIN

    for trace in traces:
        corners = trace.split(' -> ')
        for corner_index, corner in enumerate(corners):
            next_corner = corners[corner_index + 1] if corner_index + 1 < len(corners) else None
            if next_corner is None:
                break
            x, y = corner.split(',')
            x = int(x)
            y = int(y)

            next_x, next_y = next_corner.split(',')
            next_x = int(next_x)
            next_y = int(next_y)

            x_diff = next_x - x
            y_diff = next_y - y

            if x_diff < 0:
                x += x_diff
                x_diff = abs(x_diff)

            if y_diff < 0:
                y += y_diff
                y_diff = abs(y_diff)

            for i in range(0, x_diff + 1):
                for j in range(0, y_diff + 1):
                    cave[(x + i, y + j)] = WALL

    max_y = max([y for _, y in cave.keys()])
    if floor:
        max_y = max_y + 2
        min_x = min([x for x, _ in cave.keys()])
        max_x = max([x for x, _ in cave.keys()])
        for x in range(min_x - 200, max_x + 200):
            cave[(x, max_y)] = WALL


    print_cave(cave)

    sand_count = 0
    while True:
        sand = sand_origin
        settled_position = simulate_sand(cave, sand, max_y)
        if settled_position is None:
            break
        if settled_position == sand_origin:
            sand_count += 1
            cave[settled_position] = SAND
            break

        cave[settled_position] = SAND
        print_cave(cave)
        sand_count += 1

    print_cave(cave)
    return sand_count


def simulate_sand(cave: dict[tuple[int, int], str], sand_origin: tuple[int, int], max_y: int) -> tuple[int, int] | None:
    sand = sand_origin
    collision_position = trace_path(cave, sand, max_y)
    if collision_position is None:
        return None

    collision = cave[(collision_position[0], collision_position[1] + 1)]
    if collision == SAND or collision == WALL:
        # sand
        left = cave.get((collision_position[0] - 1, collision_position[1] + 1), EMPTY)
        right = cave.get((collision_position[0] + 1, collision_position[1] + 1), EMPTY)
        if left == EMPTY:
            # fall left
            return simulate_sand(cave, (collision_position[0] - 1, collision_position[1]), max_y)
        elif (left == SAND or left == WALL) and right == EMPTY:
            # fall right
            return simulate_sand(cave, (collision_position[0] + 1, collision_position[1]), max_y)
        else:
            # settle on top
            return collision_position

def trace_path(cave: dict[tuple[int, int], str], sand: tuple[int, int], max_y: int) -> tuple[int, int] | None:
    current_position = sand
    while True:
        if current_position[1] >= max_y:
            return None
        next_position = (current_position[0], current_position[1] + 1)
        if cave.get(next_position, EMPTY) != EMPTY:
            return current_position

        current_position = next_position
