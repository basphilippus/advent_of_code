import utils
from aoc_2022.day_12 import get_fewest_steps_from_start_position, get_fewest_steps_from_all_start_positions


@utils.example(2022, 12, 1, get_fewest_steps_from_start_position)
def test_example_part_1(result: int):
    assert result == 31


@utils.example(2022, 12, 2, get_fewest_steps_from_all_start_positions)
def test_example_part_2(result: int):
    assert result == 29


@utils.puzzle(2022, 12, 1, get_fewest_steps_from_start_position)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 12, 2, get_fewest_steps_from_all_start_positions)
def test_puzzle_part_2(_: int):
    pass
