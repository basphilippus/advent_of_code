import utils
from aoc_2022.day_13 import get_sum_of_indices, sort_packets


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    output = get_sum_of_indices(example_input)
    sum_of_indices = sum([i + 1 for i, correct in enumerate(output) if correct])
    print('Day 13 Example Part 1:')
    print(f'Sum of indices: {sum_of_indices}')
    print()
    assert sum_of_indices == 13


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    decoder_key = sort_packets(example_input)
    print('Day 13 Example Part 2:')
    print(f'Decoder key: {decoder_key}')
    print()
    assert decoder_key == 140

def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    output = get_sum_of_indices(puzzle_input)
    sum_of_indices = sum([i + 1 for i, correct in enumerate(output) if correct])
    print('Day 13 Puzzle Part 1:')
    print(f'Sum of indices: {sum_of_indices}')
    print()
    assert sum_of_indices == 6568


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    decoder_key = sort_packets(puzzle_input)
    print('Day 13 Puzzle Part 2:')
    print(f'Decoder key: {decoder_key}')
    print()