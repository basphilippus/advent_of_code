import utils
from aoc_2022.day_10 import get_sum_of_6_signal_strengths, get_word_output


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    sum_of_signal_strengths = get_sum_of_6_signal_strengths(example_input)
    print('Day 10 Example Part 1:')
    print(f'Sum of the 6 signal strengths: {sum_of_signal_strengths}')
    print()
    assert sum_of_signal_strengths == 0

    example_input = utils.get_example_input(__file__, 2)
    sum_of_signal_strengths = get_sum_of_6_signal_strengths(example_input)
    print('Day 10 Example Part 2 Example 2:')
    print(f'Sum of the 6 signal strengths: {sum_of_signal_strengths}')
    print()
    assert sum_of_signal_strengths == 13140


def test_example_part_2():
    example_input = utils.get_example_input(__file__, 2)
    word_output = get_word_output(example_input)
    expected_output = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
    assert word_output == expected_output

    doubled_output = ''
    for line in word_output.split('\n'):
        for character in line:
            doubled_output += character
            doubled_output += character
        doubled_output += '\n'

    print('Day 10 Example Part 2 Example 2:')
    print(f'Outputted word: \n{doubled_output}')
    print()

def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    sum_of_signal_strengths = get_sum_of_6_signal_strengths(puzzle_input)
    print('Day 9 Puzzle Part 1:')
    print(f'Sum of the 6 signal strengths: {sum_of_signal_strengths}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    word_output = get_word_output(puzzle_input)

    doubled_output = ''
    for line in word_output.split('\n'):
        for character in line:
            doubled_output += character
            doubled_output += character
        doubled_output += '\n'

    print('Day 10 Example Part 2:')
    print(f'Outputted word: \n{doubled_output}')
    print()
