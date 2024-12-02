import utils
from aoc_2022.day_11 import get_monkey_business_level


def test_example_part_1():
    example_input = utils.get_example_input(__file__)
    monkey_business_level = get_monkey_business_level(example_input, 20, True)
    print('Day 11 Example Part 1:')
    print(f'Monkey business level after 20 rounds: {monkey_business_level}')
    print()
    assert monkey_business_level == 10605


def test_example_part_2():
    example_input = utils.get_example_input(__file__)
    monkey_business_level = get_monkey_business_level(example_input, 10_000, False)
    print('Day 11 Example Part 2:')
    print(f'Monkey business level after 10,000 rounds: {monkey_business_level}')
    print()
    assert monkey_business_level == 2713310158

def test_puzzle_part_1():
    puzzle_input = utils.get_puzzle_input(__file__)
    monkey_business_level = get_monkey_business_level(puzzle_input, 20, True)
    print('Day 11 Puzzle Part 1:')
    print(f'Monkey business level after 20 rounds: {monkey_business_level}')
    print()


def test_puzzle_part_2():
    puzzle_input = utils.get_puzzle_input(__file__)
    monkey_business_level = get_monkey_business_level(puzzle_input, 10_000, False)
    print('Day 11 Puzzle Part 2:')
    print(f'Monkey business level after 10,000 rounds: {monkey_business_level}')
    print()
