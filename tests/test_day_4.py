import utils
from aoc_2022.day_4 import get_number_of_fully_contained_pairs, get_number_of_overlapping_pairs


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    number_of_pairs = get_number_of_fully_contained_pairs(example_input)
    print('Example Part 1:')
    print(f'Number of fully contained pairs: {number_of_pairs}')
    print()
    assert number_of_pairs == 2


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    number_of_pairs = get_number_of_overlapping_pairs(example_input)
    print('Example Part 2:')
    print(f'Number of pairs: {number_of_pairs}')
    print()
    assert number_of_pairs == 4


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    number_of_pairs = get_number_of_fully_contained_pairs(puzzle_input)
    print('Puzzle Part 1:')
    print(f'Number of fully contained pairs: {number_of_pairs}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    number_of_pairs = get_number_of_overlapping_pairs(puzzle_input)
    print('Example Part 2:')
    print(f'Number of pairs: {number_of_pairs}')
    print()
