import utils
from aoc_2022.day_13 import get_sum_of_indices, sort_packets


@utils.example(2022, 13, 1, get_sum_of_indices)
def test_example_part_1(result: list[int]):
    sum_of_indices = sum([i + 1 for i, correct in enumerate(result) if correct])
    assert sum_of_indices == 13


@utils.example(2022, 13, 2, sort_packets)
def test_example_part_2(result: int):
    assert result == 140


@utils.puzzle(2022, 13, 1, get_sum_of_indices)
def test_puzzle_part_1(result: list[int]):
    sum_of_indices = sum([i + 1 for i, correct in enumerate(result) if correct])
    print(f'Sum of indices: {sum_of_indices}')


@utils.puzzle(2022, 13, 2, sort_packets)
def test_puzzle_part_2(_: int):
    pass
