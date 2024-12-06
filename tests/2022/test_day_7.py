import utils
from aoc_2022.day_7 import get_sum_of_directory_sizes, get_smallest_directory_size_to_delete


@utils.example(2022, 7, 1, get_sum_of_directory_sizes, maximum_size=100000)
def test_example_part_1(result: int):
    assert result == 95437


@utils.example(2022, 7, 2, get_smallest_directory_size_to_delete, maximum_size=30000000)
def test_example_part_2(result: int):
    assert result == 24933642


@utils.puzzle(2022, 7, 1, get_sum_of_directory_sizes, maximum_size=100000)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 7, 2, get_smallest_directory_size_to_delete, maximum_size=30000000)
def test_puzzle_part_2(_: int):
    pass
