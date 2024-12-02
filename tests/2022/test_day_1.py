import utils
from aoc_2022.day_1 import sort_calorie_counts


@utils.example(2022, 1, 1, sort_calorie_counts)
def test_example_part_1(result: list[int]):
    assert result[0] == 24000


@utils.example(2022, 1, 2, sort_calorie_counts)
def test_example_part_2(result: list[int]):
    sum_of_3_highest_counts = result[0] + result[1] + result[2]
    assert sum_of_3_highest_counts == 45000


@utils.puzzle(2022, 1, 1, sort_calorie_counts)
def test_puzzle_part_1(result: list[int]):
    pass


@utils.puzzle(2022, 1, 2, sort_calorie_counts)
def test_puzzle_part_2(result: list[int]):
    sum_of_3_highest_counts = result[0] + result[1] + result[2]
    print(f'Sum of the three highest calorie counts: {sum_of_3_highest_counts}')
