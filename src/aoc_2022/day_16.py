import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_most_pressure_released(input_data: list[str], minutes: int) -> int:
    valves = {}
    for valve in input_data:
        name = valve.split(' has')[0][6:]
        flow_rate = int(valve.split(';')[0].split('=')[1])
        if 'valves' in valve:
            tunnels = valve.split('valves ')[1].split(', ')
        else:
            tunnels = [valve.split('valve ')[1]]

        valves[name] = {
            'name': name,
            'flow_rate': flow_rate,
            'tunnels': tunnels,
            'status': False
        }

    start_valve = valves['AA']
    parent_path = []
    max_pressure_released = traverse_path(valves, start_valve, 0, parent_path, minutes)
    return max_pressure_released


def traverse_path(valves: dict, start_valve: dict, max_pressure_released: int, parent_path: list, minutes: int) -> int:
    for tunnel in start_valve['tunnels']:
        next_valve = valves[tunnel]
        new_path = parent_path.copy()
        new_path.append((next_valve['name'], next_valve['flow_rate'], False))
        valve_opened = [path for path in new_path if path[0] == tunnel and path[2]]
        if next_valve['flow_rate'] > 0 and not valve_opened:
            new_path.append((next_valve['name'], next_valve['flow_rate'], True))
            if minutes - 2 == 0:
                path_total_pressure = calculate_total_pressure_released(new_path)
                if path_total_pressure > max_pressure_released:
                    max_pressure_released = path_total_pressure
                    print(max_pressure_released)
                return max_pressure_released
            else:
                max_pressure_released = traverse_path(valves, next_valve, max_pressure_released, new_path, minutes - 2)
        else:
            if minutes - 1 == 0:
                path_total_pressure = calculate_total_pressure_released(new_path)
                if path_total_pressure > max_pressure_released:
                    max_pressure_released = path_total_pressure
                    print(max_pressure_released)
                return max_pressure_released
            else:
                max_pressure_released = traverse_path(valves, next_valve, max_pressure_released, new_path, minutes - 1)

    return max_pressure_released


def calculate_total_pressure_released(path: list) -> int:
    total_pressure = 0
    open_valves = []
    for minute, valve in enumerate(path):
        if valve[2]:
            open_valves.append(valve[1])

        total_pressure += sum(open_valves)

    return total_pressure

