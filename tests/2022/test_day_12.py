import utils
from aoc_2022.day_12 import get_fewest_steps_from_start_position, get_fewest_steps_from_all_start_positions


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    fewest_steps = get_fewest_steps_from_start_position(example_input)
    print('Day 12 Example Part 1:')
    print(f'Fewest steps: {fewest_steps}')
    print()
    assert fewest_steps == 31


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    fewest_steps = get_fewest_steps_from_all_start_positions(example_input)
    print('Day 12 Example Part 2:')
    print(f'Fewest steps for all starting positions: {fewest_steps}')
    print()
    assert fewest_steps == 29

def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    fewest_steps = get_fewest_steps_from_start_position(puzzle_input)
    print('Day 12 Puzzle Part 1:')
    print(f'Fewest steps: {fewest_steps}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    fewest_steps = get_fewest_steps_from_all_start_positions(puzzle_input)
    print('Day 12 Puzzle Part 2:')
    print(f'Fewest steps for all starting positions: {fewest_steps}')
    print()
