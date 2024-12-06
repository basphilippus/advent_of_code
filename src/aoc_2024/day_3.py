import re

valid_multiplication_regex = re.compile(r"mul\(\d+,\d+\)")
disabled_memory_regex = re.compile("don't\(\).*?do\(\)")


def get_result_of_valid_multiplications(memory: list[str]) -> int:
    valid_multiplications = valid_multiplication_regex.findall("".join(memory))

    total: int = 0
    for multiplication in valid_multiplications:
        a, b = map(int, multiplication[4:-1].split(","))
        total += a * b

    return total


def get_result_of_valid_multiplications_include_disabled_memory(memory: list[str]) -> int:
    memory_string = "".join(memory)
    disabled_memory = disabled_memory_regex.finditer(memory_string)
    disabled_memory_parts = [match.span() for match in disabled_memory]
    for disabled_memory_part in reversed(disabled_memory_parts):
        memory_string = memory_string[:disabled_memory_part[0]] + memory_string[disabled_memory_part[1]:]

    valid_multiplications = get_result_of_valid_multiplications([memory_string])
    return valid_multiplications
