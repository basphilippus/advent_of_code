import os


def get_puzzle_input(filepath):
    filename = os.path.basename(filepath)
    input_file = filename.replace('test_', '').replace('py', 'txt')
    with open(f'resources/{input_file}', 'r') as f:
        puzzle_input = f.read()
    return puzzle_input.split('\n')


def get_example_input(filepath):
    filename = os.path.basename(filepath)
    input_file = filename.replace('test_', '').replace('.py', '_example.txt')
    with open(f'resources/{input_file}', 'r') as f:
        example_input = f.read()
    return example_input.split('\n')
