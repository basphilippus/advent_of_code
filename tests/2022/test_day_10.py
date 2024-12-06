import utils
from aoc_2022.day_10 import get_sum_of_6_signal_strengths, get_word_output


@utils.example(2022, 10, 1, get_sum_of_6_signal_strengths)
def test_example_part_1(result: int):
    assert result == 0


@utils.example(2022, 10, 1, get_sum_of_6_signal_strengths, 2)
def test_example_part_1_example_2(result: str):
    assert result == 13140


@utils.example(2022, 10, 2, get_word_output, 2)
def test_example_part_2(result: str):
    expected_output = """██  ██  ██  ██  ██  ██  ██  ██  ██  ██  
███   ███   ███   ███   ███   ███   ███ 
████    ████    ████    ████    ████    
█████     █████     █████     █████     
██████      ██████      ██████      ████
███████       ███████       ███████     
"""
    assert result == expected_output


@utils.puzzle(2022, 10, 1, get_sum_of_6_signal_strengths)
def test_puzzle_part_1(_: int):
    pass


@utils.puzzle(2022, 10, 2, get_word_output)
def test_puzzle_part_2(_: str):
    pass
