import utils
from aoc_2022.day_8 import get_amount_of_visible_trees, get_best_scenic_score


@utils.example(2022, 8, 1, get_amount_of_visible_trees)
def test_example_part_1(result: int):
    assert result == 21


@utils.example(2022, 8, 2, get_best_scenic_score)
def test_example_part_2(result: int):
    assert result == 8


@utils.puzzle(2022, 8, 1, get_amount_of_visible_trees)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 8, 2, get_best_scenic_score)
def test_puzzle_part_2(_: int):
    pass
