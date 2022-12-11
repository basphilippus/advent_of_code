import math
import time
from collections import defaultdict
from typing import List, Callable, Dict
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Monkey:

    def __init__(self,
                 starting_items: List[int],
                 operation: Callable[[int], int],
                 test: Callable[[int], int],
                 modulo: int):
        self.items: List[int] = starting_items
        self.operation: Callable[[int], int] = operation
        self.test: Callable[[int], int] = test
        self.modulo: int = modulo

    @staticmethod
    def parse_monkeys(monkey_notes: List[str]) -> List['Monkey']:
        monkeys: List[Monkey] = []
        monkey_note_collection: Dict[int, List[str]] = defaultdict(list)
        current_monkey: int = 0

        for monkey_note in monkey_notes:
            if not monkey_note:
                current_monkey += 1
                continue

            monkey_note_collection[current_monkey].append(monkey_note)

        for monkey_number, monkey_notes in monkey_note_collection.items():
            monkey = Monkey.parse_monkey(monkey_notes)
            monkeys.append(monkey)
        return monkeys

    @staticmethod
    def parse_monkey(monkey_notes: List[str]) -> 'Monkey':
        starting_items: List[int] = []
        operation: Callable[[int], int] = lambda x: x
        test: Callable[[int], int] = lambda x: x
        modulo: int = 0

        for monkey_note_index, monkey_note in enumerate(monkey_notes):
            if monkey_note.startswith('  Starting items: '):
                starting_items = [int(item) for item in monkey_note[18:].split(', ')]
            elif monkey_note.startswith('  Operation: '):
                operation = Monkey.parse_operation(monkey_note[13:])
            elif monkey_note.startswith('  Test: '):
                test = Monkey.parse_test(monkey_notes[monkey_note_index:])
                modulo = int(monkey_notes[monkey_note_index][21:])

        if not operation:
            raise ValueError('No operation found')
        if not test:
            raise ValueError('No test found')

        return Monkey(starting_items, operation, test, modulo)

    @staticmethod
    def parse_operation(operation: str) -> Callable[[int], int]:
        operation_parts = operation.split(' ')
        variable_1, operator, variable_2 = operation_parts[2], operation_parts[3], operation_parts[4]
        if variable_1 == 'old' and variable_2 == 'old' and operator == '*':
            return lambda old: old ** 2
        operation = eval(f'lambda old: {variable_1} {operator} {variable_2}')
        return operation

    @staticmethod
    def parse_test(test_notes: List[str]) -> Callable[[int], int]:
        divisible = int(test_notes[0].split(' ')[-1])
        true_condition = int(test_notes[1].split(' ')[-1])
        false_condition = int(test_notes[2].split(' ')[-1])
        test = eval(f'lambda test_value: {true_condition} if test_value % {divisible} == 0 else {false_condition}')
        return test


def simulate_rounds(monkeys: List[Monkey], rounds: int, divide_by_three: bool) -> int:
    monkey_items_inspected: Dict[int, int] = defaultdict(int)

    # I stole this from reddit because I don't know math that well
    product_of_operations = math.prod([monkey.modulo for monkey in monkeys])
    for round_number in range(rounds):
        logger.debug(f'Round {round_number + 1}')
        monkey_items_inspected_this_round = defaultdict(int)
        for monkey_index, monkey in enumerate(monkeys):
            while monkey.items:
                item = monkey.items.pop(0)
                worry_level = monkey.operation(item) % product_of_operations
                if divide_by_three:
                    worry_level = worry_level // 3

                item_new_monkey_index = monkey.test(worry_level)
                monkeys[item_new_monkey_index].items.append(worry_level)
                monkey_items_inspected_this_round[monkey_index] += 1

        for monkey_index, items_inspected in monkey_items_inspected_this_round.items():
            monkey_items_inspected[monkey_index] += items_inspected

        print_monkeys(round_number, monkeys)

    logger.debug('')
    for monkey_index, monkey in enumerate(monkeys):
        logger.debug(f'Monkey {monkey_index} inspected {monkey_items_inspected[monkey_index]} items')

    most_active_monkey = max(monkey_items_inspected, key=monkey_items_inspected.get)
    most_active_monkey_items_inspected = monkey_items_inspected[most_active_monkey]
    monkey_items_inspected[most_active_monkey] = 0
    second_most_active_monkey = max(monkey_items_inspected, key=monkey_items_inspected.get)
    second_most_active_monkey_items_inspected = monkey_items_inspected[second_most_active_monkey]
    return most_active_monkey_items_inspected * second_most_active_monkey_items_inspected


def print_monkeys(round_number: int, monkeys: List[Monkey]):
    if logger.level != logging.DEBUG:
        return

    logger.debug(f'After round {round_number + 1}, the monkeys are holding items with these worry levels:')
    for monkey_index, monkey in enumerate(monkeys):
        logger.debug(f'Monkey {monkey_index}: {len(monkey.items)}')

def get_monkey_business_level(monkey_notes: List[str], rounds: int, divide_by_three: bool) -> int:
    monkeys: List[Monkey] = Monkey.parse_monkeys(monkey_notes)
    monkey_business_level = simulate_rounds(monkeys, rounds, divide_by_three)
    return monkey_business_level
