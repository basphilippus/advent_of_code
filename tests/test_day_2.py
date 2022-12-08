import utils
from aoc_2022.day_2 import play_rock_paper_scissors, get_correct_rock_paper_scissors_score


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    score = play_rock_paper_scissors(example_input)
    print('Example Part 1:')
    print(f'Rock Paper Scissors score: {score}')
    print()
    assert score == 15


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    score = get_correct_rock_paper_scissors_score(example_input)
    print('Example Part 2:')
    print(f'Rock Paper Scissors score: {score}')
    print()
    assert score == 12


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    score = play_rock_paper_scissors(puzzle_input)
    print('Puzzle Part 1:')
    print(f'Rock Paper Scissors score: {score}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    score = get_correct_rock_paper_scissors_score(puzzle_input)
    print('Puzzle Part 2:')
    print(f'Rock Paper Scissors score: {score}')
    print()
