import utils
from aoc_2022.day_3 import get_sum_of_priorities, get_sum_of_priorities_for_item_types


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    sum_of_priorities = get_sum_of_priorities(example_input)
    print('Day 3 Example Part 1:')
    print(f'Sum of priorities: {sum_of_priorities}')
    print()
    assert sum_of_priorities == 157


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    sum_of_priorities = get_sum_of_priorities_for_item_types(example_input)
    print('Day 3 Example Part 2:')
    print(f'Sum of priorities: {sum_of_priorities}')
    print()
    assert sum_of_priorities == 70


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    sum_of_priorities = get_sum_of_priorities(puzzle_input)
    print('Day 3 Puzzle Part 1:')
    print(f'Sum of priorities: {sum_of_priorities}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    sum_of_priorities = get_sum_of_priorities_for_item_types(puzzle_input)
    print('Day 3 Example Part 2:')
    print(f'Sum of priorities: {sum_of_priorities}')
    print()
