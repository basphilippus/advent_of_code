import utils
from aoc_2022.day_15 import get_beacon_positions, get_tuning_frequency


@utils.example(2022, 15, 1, get_beacon_positions, position=10)
def test_example_part_1(result: int):
    assert result == 26


@utils.example(2022, 15, 2, get_tuning_frequency, max_range=20)
def test_example_part_2(result: int):
    assert result == 56000011


@utils.puzzle(2022, 15, 1, get_beacon_positions, position=2000000)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 15, 2, get_tuning_frequency, max_range=4000000)
def test_puzzle_part_2(_: int):
    pass
