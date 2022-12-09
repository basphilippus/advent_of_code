import utils
from aoc_2022.day_9 import get_amount_of_visited_positions


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    amount_of_visited_positions = get_amount_of_visited_positions(example_input, 2)
    print('Day 9 Example Part 1:')
    print(f'Amount of visited positions: {amount_of_visited_positions}')
    print()
    assert amount_of_visited_positions == 13


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    amount_of_visited_positions = get_amount_of_visited_positions(example_input, 10)
    print('Day 9 Example Part 2:')
    print(f'Amount of visited positions: {amount_of_visited_positions}')
    print()
    assert amount_of_visited_positions == 1

    example_input = utils.get_example_input(__file__, 2)
    amount_of_visited_positions = get_amount_of_visited_positions(example_input, 10)
    print('Day 9 Example Part 2 Example 2:')
    print(f'Amount of visited positions: {amount_of_visited_positions}')
    print()
    assert amount_of_visited_positions == 36


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    amount_of_visited_positions = get_amount_of_visited_positions(puzzle_input, 2)
    print('Day 9 Puzzle Part 1:')
    print(f'Amount of visited positions: {amount_of_visited_positions}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    amount_of_visited_positions = get_amount_of_visited_positions(puzzle_input, 10)
    print('Day 9 Example Part 2:')
    print(f'Amount of visited positions: {amount_of_visited_positions}')
    print()
