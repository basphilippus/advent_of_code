from typing import List, Callable, Tuple, Optional
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Program:

    def __init__(self, instructions: List[str]) -> None:
        self.instructions: List[str] = instructions
        self.variable: int = 1
        self.cycle: int = 1
        self.position: int = 0
        self.row: int = 0
        self.rows: List[str] = []
        self.signal_strengths: List[int] = []

        self.cycles_to_watch: List[int] = []
        self.resolution: Tuple[int, int] = (0, 0)

    def get_signal_strengths(self, cycles_to_watch: List[int]) -> None:
        self.cycles_to_watch = cycles_to_watch

        for instruction_index, instruction in enumerate(self.instructions):
            if not instruction:
                continue

            instruction_parts: List[str] = instruction.split(' ')
            instruction_function: Callable[[int, Optional[int]], Tuple[int, int]] = \
                getattr(self, f'execute_{instruction_parts[0]}')
            parameter: Optional[int] = None
            if len(instruction_parts) == 2:
                parameter = int(instruction_parts[1])
            instruction_function(instruction_index, parameter)

    def cycle_callback(self):
        if self.cycle in self.cycles_to_watch:
            signal_strength = self.cycle * self.variable
            logger.debug(f'Cycle {self.cycle}, variable {self.variable}: {signal_strength}')
            self.signal_strengths.append(signal_strength)
        self.cycle += 1

    def execute_noop(self, instruction_index: int, parameter: Optional[int]):
        logger.debug(f'{instruction_index}, {self.cycle}: Noop')
        if parameter:
            raise ValueError('Noop instruction does not accept parameters')
        self.cycle_callback()


    def execute_addx(self, instruction_index: int, parameter: Optional[int]):
        logger.debug(f'{instruction_index}, {self.cycle}: '
                     f'Add {parameter} to {self.variable}, result {self.variable + parameter}')
        if not parameter:
            raise ValueError('Addx instruction requires a parameter')

        self.cycle_callback()
        self.cycle_callback()
        self.variable += parameter

    def get_output(self, resolution: Tuple[int, int]) -> str:
        self.resolution = resolution
        self.rows.append('')
        self.print_sprint_position()

        for instruction in self.instructions:
            if not instruction:
                continue

            instruction_parts: List[str] = instruction.split(' ')
            instruction_function: Callable[[Optional[int]], Tuple[int, int]] =\
                getattr(self, f'draw_{instruction_parts[0]}')
            parameter: Optional[int] = None
            if len(instruction_parts) == 2:
                parameter = int(instruction_parts[1])
            instruction_function(parameter)

        return '\n'.join(self.rows)

    def draw_addx(self, parameter: Optional[int]):
        if not parameter:
            raise ValueError('Addx instruction requires a parameter')

        cycle_string: str = str(self.cycle).ljust(3)
        logger.debug(f'Start cycle {cycle_string}: begin executing addx {parameter}')
        logger.debug(f'During cycle {cycle_string}: CRT draws pixel in position {self.position}')
        self.draw_pixel()
        self.increment_position()
        logger.debug(f'Current CRT row: {self.rows[self.row]}')
        logger.debug('')

        logger.debug(f'During cycle {cycle_string}: CRT draws pixel in position {self.position}')
        self.draw_pixel()
        self.increment_position()
        logger.debug(f'Current CRT row: {self.rows[self.row]}')
        self.variable += parameter
        logger.debug(f'End of cycle {cycle_string}: '
                  f'finished executing addx {parameter} (Register X is now {self.variable})')
        self.print_sprint_position()

    def draw_noop(self, parameter: Optional[int]):
        if parameter:
            raise ValueError('Noop instruction does not accept parameters')

        cycle_string: str = str(self.cycle).ljust(3)
        logger.debug(f'Start cycle {cycle_string}: begin executing noop')
        logger.debug(f'During cycle {cycle_string}: CRT draws pixel in position {self.position}')
        self.draw_pixel()
        self.increment_position()
        logger.debug(f'Current CRT row: {self.rows[self.row]}')
        logger.debug(f'End of cycle {cycle_string}: finished executing noop')

    def draw_pixel(self) -> None:
        if self.position in {self.variable - 1, self.variable, self.variable + 1}:
            self.rows[self.row] += '#'
        else:
            self.rows[self.row] += '.'

    def increment_position(self) -> None:
        self.position += 1
        if self.position >= self.resolution[0]:
            self.position = 0
            self.row += 1
            self.rows.append('')

    def print_sprint_position(self) -> None:
        logger.debug(f'Sprite position: {"".join(["." * self.variable])}###'
              f'{"".join(["." * (self.resolution[0] - self.variable - 3)])}')
        logger.debug('')

def get_sum_of_6_signal_strengths(instructions: List[str]) -> int:
    program = Program(instructions)
    program.get_signal_strengths(cycles_to_watch=[20, 60, 100, 140, 180, 220])
    return sum(program.signal_strengths)


def get_word_output(instructions: List[str]) -> str:
    program = Program(instructions)
    output: str = program.get_output(resolution=(40, 6))
    return output