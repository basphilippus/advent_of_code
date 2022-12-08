from typing import List, Dict


DEBUG = False


def get_top_crates_for_each_stack(puzzle_input: List[str]) -> str:
    movesets_start = 0
    for line_number, line in enumerate(puzzle_input):
        if not line:
            movesets_start = line_number + 1
    crate_setup_lines = puzzle_input[:movesets_start - 1]
    stacks = setup_stacks(crate_setup_lines)
    visualize_stack(stacks)

    movesets = puzzle_input[movesets_start:]
    for moveset in movesets:
        moveset_words = moveset.split(' ')
        amount_of_creates, start_stack, end_stack = int(moveset_words[1]), int(moveset_words[3]), int(moveset_words[5])
        move_boxes(stacks, start_stack, end_stack, amount_of_creates)
        visualize_stack(stacks)

    return get_top_boxes(stacks)


def get_top_crates_for_each_stack_cratemover_9001(puzzle_input: List[str]) -> str:
    movesets_start = 0
    for line_number, line in enumerate(puzzle_input):
        if not line:
            movesets_start = line_number + 1
    crate_setup_lines = puzzle_input[:movesets_start - 1]
    stacks = setup_stacks(crate_setup_lines)
    visualize_stack(stacks)

    movesets = puzzle_input[movesets_start:]
    for moveset in movesets:
        moveset_words = moveset.split(' ')
        amount_of_creates, start_stack, end_stack = int(moveset_words[1]), int(moveset_words[3]), int(moveset_words[5])
        move_boxes_cratemover_9001(stacks, start_stack, end_stack, amount_of_creates)
        visualize_stack(stacks)

    return get_top_boxes(stacks)


def setup_stacks(stack_input: List[str]) -> Dict[int, List[str]]:
    stack_names = [int(stack) for stack in stack_input[-1].strip().split(' ') if stack]
    stacks: Dict[int, List[str]] = {stack: [] for stack in stack_names}

    for crate_setup_line in reversed(stack_input[:-1]):
        for line_index in range(len(crate_setup_line) // 4 + 1):
            crate = crate_setup_line[line_index * 4:line_index * 4 + 4].strip().strip('[').strip(']')
            if crate:
                stacks[line_index + 1].append(crate)

    return stacks


def move_boxes(stacks: Dict[int, List[str]], start_stack: int, end_stack: int, amount_of_creates: int):
    for _ in range(amount_of_creates):
        crate = stacks[start_stack].pop()
        stacks[end_stack].append(crate)


def move_boxes_cratemover_9001(stacks: Dict[int, List[str]], start_stack: int, end_stack: int, amount_of_creates: int):
    move_stack = stacks[start_stack][-amount_of_creates:]
    stacks[start_stack] = stacks[start_stack][:-amount_of_creates]
    stacks[end_stack] += move_stack


def get_top_boxes(stacks: Dict[int, List[str]]) -> str:
    top_boxes = ''
    for stack in stacks:
        top_boxes += stacks[stack][-1]
    return top_boxes


def visualize_stack(stacks: Dict[int, List[str]]):
    if not DEBUG:
        return

    print()
    max_boxes = max([len(stacks[stack]) for stack in stacks])
    for line in reversed(range(max_boxes)):
        line_string = ''
        for stack in stacks:
            if len(stacks[stack]) > line:
                line_string += f'[{stacks[stack][line]}] '
            else:
                line_string += '    '
        print(line_string)
