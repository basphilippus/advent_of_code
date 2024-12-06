import os
from typing import List, Optional, Callable


def get_puzzle_input(year: int, day: int) -> List[str]:

    project_base_path = "/".join(__file__.split('/')[:-1])
    with open(f'{project_base_path}/resources/{year}/day_{day}.txt', 'r') as f:
        puzzle_input = f.read()
    return puzzle_input.split('\n')


def get_example_input(year: int, day: int, example_number: Optional[int] = None) -> List[str]:
    if not example_number:
        example_number_string = ''
    else:
        example_number_string = f'{example_number}'

    project_base_path = "/".join(__file__.split('/')[:-1])
    with open(f'{project_base_path}/resources/{year}/day_{day}_example{example_number_string}.txt', 'r') as f:
        example_input = f.read()
    return example_input.split('\n')


def example(year: int,
            day: int,
            part: int,
            implementation: Callable = lambda x: x,
            example_number: int | None = None,
            **implementation_kwargs):
    def example_decorator(func):
        def wrapper(*args, **kwargs):
            example_input = get_example_input(year, day, example_number)
            result = implementation(example_input, **implementation_kwargs)
            print(f'Day {day} Example Part {part}:')
            if isinstance(result, str):
                print("Result:")
                print(result)
            else:
                print(f'Result: {result}')
            return func(result)
        return wrapper

    return example_decorator


def puzzle(year: int,
           day: int,
           part: int,
           implementation: Callable,
           **implementation_kwargs):
    def example_decorator(func):
        def wrapper(*args, **kwargs):
            example_input = get_puzzle_input(year, day)
            result = implementation(example_input, **implementation_kwargs)
            print(f'Day {day} Example Part {part}:')
            if isinstance(result, str):
                print("Result:")
                print(result)
            else:
                print(f'Result: {result}')
            return func(result)

        return wrapper

    return example_decorator
