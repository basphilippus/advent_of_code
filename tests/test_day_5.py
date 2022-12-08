import utils
from aoc_2022.day_5 import get_top_crates_for_each_stack, get_top_crates_for_each_stack_cratemover_9001


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    top_crates = get_top_crates_for_each_stack(example_input)
    print('Example Part 1:')
    print(f'Top crates for each stack: {top_crates}')
    print()
    assert top_crates == 'CMZ'


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    top_crates = get_top_crates_for_each_stack_cratemover_9001(example_input)
    print('Example Part 2:')
    print(f'Top crates for each stack: {top_crates}')
    print()
    assert top_crates == 'MCD'


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    top_crates = get_top_crates_for_each_stack(puzzle_input)
    print('Puzzle Part 1:')
    print(f'Top crates for each stack: {top_crates}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    top_crates = get_top_crates_for_each_stack_cratemover_9001(puzzle_input)
    print('Example Part 2:')
    print(f'Top crates for each stack: {top_crates}')
    print()
