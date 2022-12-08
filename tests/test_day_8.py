import utils
from aoc_2022.day_8 import get_amount_of_visible_trees, get_best_scenic_score


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    amount_of_visible_trees = get_amount_of_visible_trees(example_input)
    print('Example Part 1:')
    print(f'Amount of visible trees: {amount_of_visible_trees}')
    print()
    assert amount_of_visible_trees == 21


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    best_tree = get_best_scenic_score(example_input)
    print('Example Part 2:')
    print(f'Tree with the best scenic score: {best_tree}')
    print()
    assert best_tree == 8


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    amount_of_visible_trees = get_amount_of_visible_trees(puzzle_input)
    print('Puzzle Part 1:')
    print(f'Amount of visible trees: {amount_of_visible_trees}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    best_tree = get_best_scenic_score(puzzle_input)
    print('Example Part 2:')
    print(f'Tree with the best scenic score: {best_tree}')
    print()
