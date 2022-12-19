import utils
from aoc_2022.day_15 import get_beacon_positions, get_tuning_frequency


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    beacon_count = get_beacon_positions(example_input, position=10)
    print('Day 15 Example Part 1:')
    print(f'Positions that cannot contain a beacon: {beacon_count}')
    print()
    assert beacon_count == 26


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    tuning_frequency = get_tuning_frequency(example_input, max_range=20)
    print('Day 15 Example Part 2:')
    print(f'Tuning frequency: {tuning_frequency}')
    print()
    assert tuning_frequency == 56000011

def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    beacon_count = get_beacon_positions(puzzle_input, position=2000000)
    print('Day 15 Puzzle Part 1:')
    print(f'Positions that cannot contain a beacon: {beacon_count}')
    print()
    assert beacon_count == 4985193


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    tuning_frequency = get_tuning_frequency(puzzle_input, max_range=4000000)
    print('Day 15 Puzzle Part 2:')
    print(f'Tuning frequency: {tuning_frequency}')
    print()