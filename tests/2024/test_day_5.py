import utils
from aoc_2024.day_5 import get_middle_page_number_total, get_corrected_middle_page_number_total


@utils.example(2024, 5, 1, get_middle_page_number_total)
def test_example_part_1(result: int):
    assert result == 143


@utils.example(2024, 5, 2, get_corrected_middle_page_number_total)
def test_example_part_2(result: int):
    assert result == 123


@utils.puzzle(2024, 5, 1, get_middle_page_number_total)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2024, 5, 2, get_corrected_middle_page_number_total)
def test_puzzle_part_2(_: int):
    pass
