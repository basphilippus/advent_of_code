from typing import List, Tuple, Set, Dict
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


MOVEMENT_MAP: Dict[str, Tuple[int, int]] = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}


def get_amount_of_visited_positions(movement_input: List[str], number_of_knots: int) -> int:
    start_position: Tuple[int, int] = (0, 0)
    rope: List[Tuple[int, int]] = [start_position] * number_of_knots
    visited_positions: Set[Tuple[int, int]] = {start_position}
    visualize_map(rope, visited_positions)

    for movement in movement_input:
        direction, amount = movement.split(' ')
        movement_vector: Tuple[int, int] = MOVEMENT_MAP[direction]
        for _ in range(int(amount)):
            current_position_head = (
                rope[0][0] + movement_vector[0],
                rope[0][1] + movement_vector[1]
            )
            rope[0] = current_position_head

            logger.debug('Head moved')
            visualize_map(rope, visited_positions)

            for knot_index in range(1, number_of_knots):
                current_knot = rope[knot_index]
                previous_knot = rope[knot_index - 1]
                if not is_touching_tail(previous_knot, current_knot):
                    tail_movement_x: int = previous_knot[0] - current_knot[0]
                    if tail_movement_x >= 1:
                        tail_movement_x = 1
                    elif tail_movement_x <= -1:
                        tail_movement_x = -1

                    tail_movement_y: int = previous_knot[1] - current_knot[1]
                    if tail_movement_y >= 1:
                        tail_movement_y = 1
                    elif tail_movement_y <= -1:
                        tail_movement_y = -1

                    tail_movement_vector: Tuple[int, int] = (
                        tail_movement_x,
                        tail_movement_y
                    )
                    rope[knot_index] = (
                        current_knot[0] + tail_movement_vector[0],
                        current_knot[1] + tail_movement_vector[1]
                    )
                    logger.debug(f'Moving tail with {tail_movement_vector}')

            visited_positions.add(rope[-1])

            logger.debug('Tail moved')
            visualize_map(rope, visited_positions)

    visualize_map(rope, visited_positions)
    return len(visited_positions)


def is_touching_tail(current_position_head: Tuple[int, int],
                     current_position_tail: Tuple[int, int]) -> bool:
    if current_position_head[0] == current_position_tail[0] and current_position_head[1] == current_position_tail[1]:
        return True

    x_diff = abs(current_position_tail[0] - current_position_head[0])
    y_diff = abs(current_position_tail[1] - current_position_head[1])

    # If the difference in x or y is at most 1, the head is touching the tail
    return 1 >= x_diff >= -1 and 1 >= y_diff >= -1


def visualize_map(rope: List[Tuple[int, int]],
                  visited_positions: Set[Tuple[int, int]]) -> None:
    if logger.level != logging.DEBUG:
        return

    min_x: int = min([position[0] for position in visited_positions.union(set(rope))])
    min_y: int = min([position[1] for position in visited_positions.union(set(rope))])
    max_x: int = max([position[0] for position in visited_positions] + [5])
    max_y: int = max([position[1] for position in visited_positions] + [4])

    logger.debug('')
    for y in range(max_y, min_y - 1, -1):
        line: str = ''
        for x in range(min_x, max_x + 1):
            for knot_index, position in enumerate(rope):
                if position == (x, y):
                    if knot_index == 0:
                        line += 'H'
                    else:
                        line += str(knot_index)
                    break
            else:
                if (x, y) == (0, 0):
                    line += 's'
                elif (x, y) in visited_positions:
                    line += 'X'
                else:
                    line += '.'
        logger.debug(line)
    logger.debug('')
