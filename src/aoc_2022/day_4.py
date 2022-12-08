from typing import List


DEBUG = False


def get_number_of_fully_contained_pairs(pair_input: List[str]) -> int:
    max_number = 0
    for pair in pair_input:
        first_elf, second_elf = pair.split(',')
        first_elf_numbers = [int(number) for number in first_elf.split('-')]
        second_elf_numbers = [int(number) for number in second_elf.split('-')]
        for elf_number in first_elf_numbers:
            if elf_number > max_number:
                max_number = elf_number
        for elf_number in second_elf_numbers:
            if elf_number > max_number:
                max_number = elf_number

    amount_of_fully_contained_pairs = 0
    for pair in pair_input:
        first_elf, second_elf = pair.split(',')
        first_elf_numbers = [int(number) for number in first_elf.split('-')]
        second_elf_numbers = [int(number) for number in second_elf.split('-')]

        print()
        visualize_pair(first_elf_numbers, max_number)
        visualize_pair(second_elf_numbers, max_number)

        if first_elf_numbers[0] >= second_elf_numbers[0] and first_elf_numbers[1] <= second_elf_numbers[1]:
            amount_of_fully_contained_pairs += 1
        elif second_elf_numbers[0] >= first_elf_numbers[0] and second_elf_numbers[1] <= first_elf_numbers[1]:
            amount_of_fully_contained_pairs += 1

    return amount_of_fully_contained_pairs


def get_number_of_overlapping_pairs(pair_input: List[str]) -> int:
    amount_of_overlapping_pairs = 0
    for pair in pair_input:
        first_elf, second_elf = pair.split(',')
        first_elf_numbers = [int(number) for number in first_elf.split('-')]
        second_elf_numbers = [int(number) for number in second_elf.split('-')]

        if second_elf_numbers[0] <= first_elf_numbers[1] <= second_elf_numbers[1]:
            amount_of_overlapping_pairs += 1
        elif first_elf_numbers[0] <= second_elf_numbers[1] <= first_elf_numbers[1]:
            amount_of_overlapping_pairs += 1

    return amount_of_overlapping_pairs


def visualize_pair(elf_numbers: List[int], max_number: int):
    if not DEBUG:
        return

    pair_visualization = ''
    for number in range(1, max_number + 1):
        if number < elf_numbers[0] or number > elf_numbers[1]:
            pair_visualization += '.'.rjust(3, ' ')
        else:
            pair_visualization += f'{number}'.rjust(3, ' ')
    pair_visualization += f'  {elf_numbers[0]}-{elf_numbers[1]}'
    print(pair_visualization)
