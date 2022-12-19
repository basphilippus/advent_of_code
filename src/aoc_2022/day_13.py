import logging
import re
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

split_regex = re.compile(r'(\d+)|(\[)|,|(\])')


def parse_packet(packet: str) -> list[Any]:
    parsed_packet = None
    parent_stack = []
    for index, character in enumerate([c for c in split_regex.split(packet) if c]):
        if character == '[':
            new_parsed_packet = []
            if parsed_packet is not None:
                parsed_packet.append(new_parsed_packet)
            else:
                parsed_packet = new_parsed_packet
            parent_stack.append(parsed_packet)
            parsed_packet = new_parsed_packet
        elif character == ']':
            parsed_packet = parent_stack.pop()
        else:
            parsed_packet.append(int(character))

    return parsed_packet

def compare(left: list[Any], right: list[Any], indent: int = 0) -> bool | None:
    for packet_index, packet in enumerate(left):
        left_comparison = left[packet_index]
        try:
            right_comparison = right[packet_index]
        except IndexError:
            logger.debug(f'{" " * indent}    - Right side ran out of items, so inputs are not in the right order')
            return False
        logger.debug(f'{" " * indent}    - Compare {left_comparison} vs {right_comparison}')
        if isinstance(left_comparison, int) and isinstance(right_comparison, int):
            if left_comparison < right_comparison:
                logger.debug(f'{" " * indent}        - Left side is smaller, so inputs are in the right order')
                return True
            elif left_comparison > right_comparison:
                logger.debug(f'{" " * indent}        - Right side is smaller, so inputs are not in the right order')
                return False
        elif isinstance(left_comparison, list) and isinstance(right_comparison, list):
            correct_order = compare(left_comparison, right_comparison, indent + 6)
            if correct_order is not None:
                return correct_order
        elif isinstance(left_comparison, int) and isinstance(right_comparison, list):
            logger.debug(f'{" " * indent}        - Mixed types; convert left to [{left_comparison}] and retry comparison')
            logger.debug(f'{" " * indent}        - Compare [{left_comparison}] vs {right_comparison}')
            correct_order = compare([left_comparison], right_comparison, indent + 6)
            if correct_order is not None:
                return correct_order
        elif isinstance(left_comparison, list) and isinstance(right_comparison, int):
            logger.debug(f'{" " * indent}        - Mixed types; convert right to [{right_comparison}] and retry comparison')
            logger.debug(f'{" " * indent}        - Compare {left_comparison} vs [{right_comparison}]')
            correct_order = compare(left_comparison, [right_comparison], indent + 6)
            if correct_order is not None:
                return correct_order

    if len(left) < len(right):
        logger.debug(f'{" " * indent}    - Left side ran out of items, so inputs are in the right order')
        return True
    elif len(left) > len(right):
        logger.debug(f'{" " * indent}    - Right side ran out of items, so inputs are not in the right order')
        return False

    return None


def get_sum_of_indices(packets: list[str]) -> list[bool]:
    pairs = []
    pair = []
    for packet in packets:
        if not packet:
            pairs.append(pair)
            pair = []
            continue

        parsed_packet = parse_packet(packet)
        pair.append(parsed_packet)
    pairs.append(pair)

    correctness = []
    for pair_index, pair in enumerate(pairs):
        left_packet = pair[0]
        right_packet = pair[1]
        logger.debug(f'== Pair {pair_index + 1} ==')
        logger.debug(f'- Compare {left_packet} vs {right_packet}')
        right_order = compare(left_packet, right_packet)
        correctness.append(right_order)
        logger.debug(right_order)
        logger.debug('')
    return correctness


def sort_packets(packets: list[str]) -> int:
    divider_1 = [[2]]
    divider_2 = [[6]]
    parsed_packets = [divider_1, divider_2]
    for packet in packets:
        if not packet:
            continue

        parsed_packets.append(parse_packet(packet))

    while True:
        packets_sorted = True
        for packet_index, packet in enumerate(parsed_packets):
            if packet_index == len(parsed_packets) - 1:
                break

            left_packet = packet
            right_packet = parsed_packets[packet_index + 1]
            logger.debug(f'- Compare {left_packet} vs {right_packet}')
            right_order = compare(left_packet, right_packet)
            if right_order is False:
                logger.debug(f'    - Swap {left_packet} and {right_packet}')
                parsed_packets[packet_index] = right_packet
                parsed_packets[packet_index + 1] = left_packet
                packets_sorted = False
        if packets_sorted:
            break

    divider_1_index = parsed_packets.index(divider_1)
    divider_2_index = parsed_packets.index(divider_2)

    return (divider_1_index + 1) * (divider_2_index + 1)
