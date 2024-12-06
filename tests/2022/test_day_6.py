import utils
from aoc_2022.day_6 import get_markers


@utils.example(2022, 6, 1, get_markers, marker_size=4)
def test_example_part_1(result: list[int]):
    assert result == [7, 5, 6, 10, 11]


@utils.example(2022, 6, 2, get_markers, marker_size=14)
def test_example_part_2(result: list[int]):
    assert result == [19, 23, 23, 29, 26]


@utils.puzzle(2022, 6, 1, get_markers, marker_size=4)
def test_puzzle_part_1(_: list[int]):
    pass


@utils.puzzle(2022, 6, 2, get_markers, marker_size=14)
def test_puzzle_part_2(_: list[int]):
    pass
