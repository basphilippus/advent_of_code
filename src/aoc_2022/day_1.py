from typing import List


def sort_calorie_counts(elf_input: List[str]) -> List[int]:
    calorie_counts: List[int] = []
    current_elf_calorie_count = 0
    for line in elf_input:
        if not line:
            calorie_counts.append(current_elf_calorie_count)
            current_elf_calorie_count = 0
            continue

        current_elf_calorie_count += int(line)
    if current_elf_calorie_count > 0:
        calorie_counts.append(current_elf_calorie_count)
    return sorted(calorie_counts, reverse=True)
