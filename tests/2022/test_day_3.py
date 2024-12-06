import utils
from aoc_2022.day_3 import get_sum_of_priorities, get_sum_of_priorities_for_item_types


@utils.example(2022, 3, 1, get_sum_of_priorities)
def test_example_part_1(result: int):
    assert result == 157


@utils.example(2022, 3, 2, get_sum_of_priorities_for_item_types)
def test_example_part_2(result: int):
    assert result == 70


@utils.puzzle(2022, 3, 1, get_sum_of_priorities)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 3, 2, get_sum_of_priorities_for_item_types)
def test_puzzle_part_2(_: int):
    pass
