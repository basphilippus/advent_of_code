import utils
from aoc_2024.day_2 import get_amount_of_safe_reports


@utils.example(2024, 2, 1, get_amount_of_safe_reports)
def test_example_part_1(result: int):
    assert result == 2


@utils.example(2024, 2, 2, get_amount_of_safe_reports, tolerate_bad_levels=2)
def test_example_part_2(result: int):
    assert result == 4


@utils.puzzle(2024, 2, 1, get_amount_of_safe_reports)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2024, 2, 2, get_amount_of_safe_reports, tolerate_bad_levels=2)
def test_puzzle_part_2(_: int):
    pass
