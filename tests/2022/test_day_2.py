import utils
from aoc_2022.day_2 import play_rock_paper_scissors, get_correct_rock_paper_scissors_score


@utils.example(2022, 2, 1, play_rock_paper_scissors)
def test_example_part_1(result: int):
    assert result == 15


@utils.example(2022, 2, 2, get_correct_rock_paper_scissors_score)
def test_example_part_2(result: int):
    assert result == 12


@utils.puzzle(2022, 2, 1, play_rock_paper_scissors)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 2, 2, get_correct_rock_paper_scissors_score)
def test_puzzle_part_2(_: int):
    pass
