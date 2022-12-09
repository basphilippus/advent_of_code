import utils
from aoc_2022.day_1 import sort_calorie_counts


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    calorie_counts = sort_calorie_counts(example_input)
    print('Day 1 Example Part 1:')
    print(f'Elf with the highest calorie count: {calorie_counts[0]}')
    print()
    assert calorie_counts[0] == 24000


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    calorie_counts = sort_calorie_counts(example_input)
    sum_of_3_highest_counts = calorie_counts[0] + calorie_counts[1] + calorie_counts[2]
    print('Day 1 Example Part 2:')
    print(f'Sum of the three highest calorie counts: {sum_of_3_highest_counts}')
    print()
    assert sum_of_3_highest_counts == 45000


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    calorie_counts = sort_calorie_counts(puzzle_input)
    print('Day 1 Puzzle Part 1')
    print(f'Elf with the highest calorie count: {calorie_counts[0]}')


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    calorie_counts = sort_calorie_counts(puzzle_input)
    sum_of_3_highest_counts = calorie_counts[0] + calorie_counts[1] + calorie_counts[2]
    print('Day 1 Puzzle Part 2:')
    print(f'Sum of the three highest calorie counts: {sum_of_3_highest_counts}')
    print()
