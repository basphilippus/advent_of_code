import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


EMPTY = '.'
SIGNAL = '#'
BEACON = 'B'
SENSOR = 'S'


def get_beacon_map(beacon_positions: list[str]) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], str]]:
    beacon_map = {}
    sensor_map = {}
    for beacon_position in beacon_positions:
        sensor_string, closest_beacon_string = beacon_position.split(':')
        sensor_x = int(sensor_string.split(',')[0][12:])
        sensor_y = int(sensor_string.split(',')[1][3:])

        closest_beacon_x = int(closest_beacon_string.split(',')[0][24:])
        closest_beacon_y = int(closest_beacon_string.split(',')[1][3:])
        beacon_map[(closest_beacon_x, closest_beacon_y)] = BEACON

        manhattan_distance = abs(sensor_x - closest_beacon_x) + abs(sensor_y - closest_beacon_y)
        sensor_map[(sensor_x, sensor_y)] = manhattan_distance

    return sensor_map, beacon_map


def is_location_clear(sensor_map: dict[tuple[int, int], int],
                      beacon_map: dict[tuple[int, int], str],
                      x: int,
                      y: int) -> bool:
    for signal_x, signal_y in sensor_map.keys():
        distance = abs(x - signal_x) + abs(y - signal_y)
        manhattan_distance = sensor_map[(signal_x, signal_y)]
        if distance <= manhattan_distance and (x, y) not in beacon_map:
            return False

    return True

def get_beacon_positions(beacon_positions: list[str], position: int) -> int:
    sensor_map, beacon_map = get_beacon_map(beacon_positions)

    min_x = min(x - sensor_map[(x, y)] for x, y in sensor_map)
    max_x = max(x + sensor_map[(x, y)] for x, y in sensor_map)

    signal_location_count = 0
    for x in range(min_x, max_x):
        if not is_location_clear(sensor_map, beacon_map, x, position):
            signal_location_count += 1

    return signal_location_count


def get_tuning_frequency(beacon_positions: list[str], max_range: int) -> int:
    sensor_map, beacon_map = get_beacon_map(beacon_positions)

    locations_to_check = []
    for sensor_x, sensor_y in sensor_map.keys():
        manhattan_distance = sensor_map[(sensor_x, sensor_y)]
        width = 1

        locations_to_check.append((sensor_x, sensor_y - manhattan_distance - 1))
        locations_to_check.append((sensor_x, sensor_y + manhattan_distance + 1))
        for y in range(sensor_y - manhattan_distance, sensor_y + manhattan_distance + 1):
            locations_to_check.append((sensor_x - width, y))
            locations_to_check.append((sensor_x + width, y))
            if y < sensor_y:
                width += 1
            else:
                width -= 1

    for x, y in locations_to_check:
        if x < 0 or y < 0:
            continue
        if x > max_range or y > max_range:
            continue

        if is_location_clear(sensor_map, beacon_map, x, y) and (x, y) not in beacon_map:
            return x * 4000000 + y
