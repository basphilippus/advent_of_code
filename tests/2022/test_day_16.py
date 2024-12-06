import utils
from aoc_2022.day_16 import get_most_pressure_released


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    most_pressure_released = get_most_pressure_released(example_input, minutes=30)
    print('Day 16 Example Part 1:')
    print(f'Most pressure released after 30 minutes : {most_pressure_released}')
    print()
    assert most_pressure_released == 1651


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    tuning_frequency = get_tuning_frequency(example_input, max_range=20)
    print('Day 16 Example Part 2:')
    print(f'Tuning frequency: {tuning_frequency}')
    print()
    assert tuning_frequency == 56000011


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    most_pressure_released = get_most_pressure_released(puzzle_input, minutes=30)
    print('Day 16 Example Part 1:')
    print(f'Most pressure released after 30 minutes : {most_pressure_released}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    tuning_frequency = get_tuning_frequency(puzzle_input, max_range=4000000)
    print('Day 16 Puzzle Part 2:')
    print(f'Tuning frequency: {tuning_frequency}')
    print()


@utils.example(2022, 16, 1, get_most_pressure_released, minutes=30)
def test_example_part_1(result: int):
    assert result == 1651


# @utils.example(2022, 16, 2, get_tuning_frequency, max_range=20)
# def test_example_part_2(result: int):
#     assert result == 56000011


@utils.puzzle(2022, 16, 1, get_most_pressure_released, minutes=30)
def test_puzzle_part_1(_: int):
    pass


# @utils.puzzle(2022, 16, 2, get_tuning_frequency, max_range=4000000)
# def test_puzzle_part_2(_: int):
#     pass
