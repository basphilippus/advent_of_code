import utils
from aoc_2022.day_14 import count_sand


@utils.example(2022, 14, 1, count_sand)
def test_example_part_1(result: int):
    assert result == 24


@utils.example(2022, 14, 2, count_sand, floor=True)
def test_example_part_2(result: int):
    assert result == 93


@utils.puzzle(2022, 14, 1, count_sand)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 14, 2, count_sand, floor=True)
def test_puzzle_part_2(_: int):
    pass
