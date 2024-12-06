import utils
from aoc_2022.day_4 import get_number_of_fully_contained_pairs, get_number_of_overlapping_pairs


@utils.example(2022, 4, 1, get_number_of_fully_contained_pairs)
def test_example_part_1(result: int):
    assert result == 2


@utils.example(2022, 4, 2, get_number_of_overlapping_pairs)
def test_example_part_2(result: int):
    assert result == 4


@utils.puzzle(2022, 4, 1, get_number_of_fully_contained_pairs)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 4, 2, get_number_of_overlapping_pairs)
def test_puzzle_part_2(_: int):
    pass
