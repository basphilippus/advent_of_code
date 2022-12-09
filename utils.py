import os
from typing import List, Optional


def get_puzzle_input(filepath: str) -> List[str]:
    filename = os.path.basename(filepath)
    input_file = filename.replace('test_', '').replace('py', 'txt')
    with open(f'resources/{input_file}', 'r') as f:
        puzzle_input = f.read()
    return puzzle_input.split('\n')


def get_example_input(filepath: str, example_number: Optional[int] = None) -> List[str]:
    if not example_number:
        example_number_string = ''
    else:
        example_number_string = f'{example_number}'
    filename = os.path.basename(filepath)
    input_file = filename.replace('test_', '').replace('.py', f'_example{example_number_string}.txt')
    with open(f'resources/{input_file}', 'r') as f:
        example_input = f.read()
    return example_input.split('\n')
