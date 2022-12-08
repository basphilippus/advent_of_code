from typing import List


def get_sum_of_priorities(rucksack_input: List[str]) -> int:
    sum_of_priorities = 0
    for rucksack in rucksack_input:
        left_half, right_half = rucksack[0:int(len(rucksack) / 2)], rucksack[int(len(rucksack) / 2):len(rucksack)]
        duplicate_items = set(left_half).intersection(set(right_half))
        item_priorities = [get_item_priority(item) for item in duplicate_items]
        sum_of_priorities += sum(item_priorities)

    return sum_of_priorities


def get_item_priority(item: str) -> int:
    if item.lower() == item:
        # lowercase items
        return ord(item) - 96
    else:
        # uppercase items
        return ord(item) - 38


def get_sum_of_priorities_for_item_types(rucksack_input: List[str]) -> int:
    sum_of_priorities = 0
    for i in range(len(rucksack_input) // 3):
        group = rucksack_input[i * 3:(i + 1) * 3]
        duplicate_items = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        item_priorities = [get_item_priority(item) for item in duplicate_items]
        sum_of_priorities += sum(item_priorities)

    return sum_of_priorities
