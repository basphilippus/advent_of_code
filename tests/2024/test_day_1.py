import utils
from aoc_2024.day_1 import calculate_total_distance, calculate_similarity_score


@utils.example(2024, 1, 1, calculate_total_distance)
def test_example_part_1(result: int):
    assert result == 11


@utils.example(2024, 1, 2, calculate_similarity_score)
def test_example_part_2(result: int):
    assert result == 31


@utils.puzzle(2024, 1, 1, calculate_total_distance)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2024, 1, 2, calculate_similarity_score)
def test_puzzle_part_2(_: int):
    pass
