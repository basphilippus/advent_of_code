import utils
from aoc_2024.day_3 import (get_result_of_valid_multiplications,
                            get_result_of_valid_multiplications_include_disabled_memory)


@utils.example(2024, 3, 1, get_result_of_valid_multiplications)
def test_example_part_1(result: int):
    assert result == 161


@utils.example(2024, 3, 2, get_result_of_valid_multiplications_include_disabled_memory, example_number=2)
def test_example_part_2(result: int):
    assert result == 48


@utils.puzzle(2024, 3, 1, get_result_of_valid_multiplications)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2024, 3, 2, get_result_of_valid_multiplications_include_disabled_memory)
def test_puzzle_part_2(_: int):
    pass
