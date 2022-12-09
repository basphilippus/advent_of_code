import utils
from aoc_2022.day_6 import get_markers


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    start_of_packet_markers = get_markers(example_input, 4)
    print('Day 6 Example Part 1:')
    print(f'Start-of-packet markers: {start_of_packet_markers}')
    print()
    assert start_of_packet_markers == [7, 5, 6, 10, 11]


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    start_of_message_markers = get_markers(example_input, 14)
    print('Day 6 Example Part 2:')
    print(f'Start-of-message markers: {start_of_message_markers}')
    print()
    assert start_of_message_markers == [19, 23, 23, 29, 26]


def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    start_of_packet_markers = get_markers(puzzle_input, 4)
    print('Day 6 Puzzle Part 1:')
    print(f'Start-of-packet markers: {start_of_packet_markers}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    start_of_message_markers = get_markers(puzzle_input, 14)
    print('Day 6 Puzzle Part 2:')
    print(f'Start-of-message markers: {start_of_message_markers}')
    print()
