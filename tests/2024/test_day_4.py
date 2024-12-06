import utils
from aoc_2024.day_4 import get_amount_of_xmas_occurrences, get_amount_of_xmas_shapes


@utils.example(2024, 4, 1, get_amount_of_xmas_occurrences)
def test_example_part_1(result: int):
    assert result == 18


@utils.example(2024, 4, 2, get_amount_of_xmas_shapes)
def test_example_part_2(result: int):
    assert result == 9


@utils.puzzle(2024, 4, 1, get_amount_of_xmas_occurrences)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2024, 4, 2, get_amount_of_xmas_shapes)
def test_puzzle_part_2(_: int):
    pass
