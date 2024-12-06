import utils
from aoc_2022.day_9 import get_amount_of_visited_positions


@utils.example(2022, 9, 1, get_amount_of_visited_positions, number_of_knots=2)
def test_example_part_1(result: int):
    assert result == 13


@utils.example(2022, 9, 2, get_amount_of_visited_positions, number_of_knots=10)
def test_example_part_2(result: int):
    assert result == 1


@utils.puzzle(2022, 9, 1, get_amount_of_visited_positions, number_of_knots=2)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 9, 2, get_amount_of_visited_positions, number_of_knots=10)
def test_puzzle_part_2(_: int):
    pass
