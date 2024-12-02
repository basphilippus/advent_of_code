import utils
from aoc_2022.day_14 import count_sand


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    sand_count = count_sand(example_input)
    print('Day 14 Example Part 1:')
    print(f'Units of sand tha came to rest before sand started flowing into the abyss: {sand_count}')
    print()
    assert sand_count == 24


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    sand_count = count_sand(example_input, floor=True)
    print('Day 14 Example Part 2:')
    print(f'Units of sand tha came to rest before sand started flowing into the abyss: {sand_count}')
    print()
    assert sand_count == 93

def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    sand_count = count_sand(puzzle_input)
    print('Day 14 Puzzle Part 1:')
    print(f'Units of sand tha came to rest before sand started flowing into the abyss: {sand_count}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    sand_count = count_sand(puzzle_input, floor=True)
    print('Day 14 Puzzle Part 2:')
    print(f'Units of sand tha came to rest before sand started flowing into the abyss: {sand_count}')
    print()