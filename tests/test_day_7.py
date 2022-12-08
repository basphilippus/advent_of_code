import utils
from aoc_2022.day_7 import get_sum_of_directory_sizes, get_smallest_directory_size_to_delete


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    sum_of_directory_sizes = get_sum_of_directory_sizes(example_input, 100000)
    print('Example Part 1:')
    print(f'Sum of directory sizes: {sum_of_directory_sizes}')
    print()
    assert sum_of_directory_sizes == 95437


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    smallest_directory_size = get_smallest_directory_size_to_delete(example_input, 30000000)
    print('Example Part 2:')
    print(f'Smallest directory size to delete: {smallest_directory_size}')
    print()
    assert smallest_directory_size == 24933642


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    sum_of_directory_sizes = get_sum_of_directory_sizes(puzzle_input, 100000)
    print('Puzzle Part 1:')
    print(f'Sum of directory sizes: {sum_of_directory_sizes}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    smallest_directory_size = get_smallest_directory_size_to_delete(puzzle_input, 30000000)
    print('Example Part 2:')
    print(f'Smallest directory size to delete: {smallest_directory_size}')
    print()
