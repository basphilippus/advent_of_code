import utils
from aoc_2022.day_5 import get_top_crates_for_each_stack, get_top_crates_for_each_stack_cratemover_9001


@utils.example(2022, 5, 1, get_top_crates_for_each_stack)
def test_example_part_1(result: str):
    assert result == 'CMZ'


@utils.example(2022, 5, 2, get_top_crates_for_each_stack_cratemover_9001)
def test_example_part_2(result: str):
    assert result == 'MCD'


@utils.puzzle(2022, 5, 1, get_top_crates_for_each_stack)
def test_puzzle_part_1(_: str):
    pass


@utils.puzzle(2022, 5, 2, get_top_crates_for_each_stack_cratemover_9001)
def test_puzzle_part_2(_: str):
    pass
