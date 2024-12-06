import utils
from aoc_2022.day_11 import get_monkey_business_level


@utils.example(2022, 11, 1, get_monkey_business_level, rounds=20, divide_by_three=True)
def test_example_part_1(result: int):
    assert result == 10605


@utils.example(2022, 11, 2, get_monkey_business_level, rounds=10_000, divide_by_three=False)
def test_example_part_2(result: int):
    assert result == 2713310158


@utils.puzzle(2022, 11, 1, get_monkey_business_level, rounds=20, divide_by_three=True)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 11, 2, get_monkey_business_level, rounds=10_000, divide_by_three=False)
def test_puzzle_part_2(_: int):
    pass
