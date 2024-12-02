def check_report(levels: list[int]) -> int:
    increasing_levels: list[int] = []
    decreasing_levels: list[int] = []
    same_levels: list[int] = []
    large_gaps: list[int] = []

    for level_index, level in enumerate(levels):
        previous_level = levels[level_index - 1] if level_index > 0 else None

        if previous_level is not None:
            if level < previous_level:
                decreasing_levels.extend([level_index - 1, level_index])
            elif level > previous_level:
                increasing_levels.extend([level_index - 1, level_index])
            else:
                same_levels.extend([level_index - 1, level_index])

            if abs(level - previous_level) > 3:
                large_gaps.extend([level_index - 1, level_index])

    bad_levels: list[int] = []
    if large_gaps:
        bad_levels.extend(large_gaps)

    if increasing_levels and decreasing_levels:
        bad_levels.extend(increasing_levels)
        bad_levels.extend(decreasing_levels)

    if same_levels:
        bad_levels.extend(same_levels)

    return bad_levels


def get_amount_of_safe_reports(reports: list[str], tolerate_bad_levels: int = 0) -> int:
    safe_reports: int = 0
    for report in reports:
        levels: list[int] = [int(report) for report in report.split(' ')]
        bad_levels: list[int] = check_report(levels)

        if tolerate_bad_levels > 0:
            for bad_level in bad_levels:
                altered_report = levels.copy()
                altered_report.pop(bad_level)
                altered_bad_levels: list[int] = check_report(altered_report)
                if len(altered_bad_levels) == 0:
                    bad_levels = altered_bad_levels
                    break

        if len(bad_levels) == 0:
            safe_reports += 1

    return safe_reports
