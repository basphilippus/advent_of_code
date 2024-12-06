def _get_page_ordering_rules_page_updates(page_information: list[str]) -> tuple[dict[int, list[int]], list[list[int]]]:
    page_ordering_rules: dict[int, list[int]] = {}
    line_index = 0
    for line_index, page_info in enumerate(page_information):
        if page_info == "":
            break

        before_number, after_number = map(int, page_info.split("|"))
        if not page_ordering_rules.get(after_number):
            page_ordering_rules[after_number] = []

        page_ordering_rules[after_number].append(before_number)

    page_updates: list[list[int]] = []
    for page_info in page_information[line_index + 1:]:
        page_updates.append(list(map(int, page_info.split(","))))

    return page_ordering_rules, page_updates


def _get_valid_invalid_page_updates(page_ordering_rules: dict[int, list[int]],
                                    page_updates: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    valid_page_updates: list[list[int]] = []
    invalid_page_updates: list[list[int]] = []
    for page_update in page_updates:

        valid_page = True
        for page_index, page_number in enumerate(page_update):
            remaining_pages = page_update[page_index + 1:]
            if page_number in page_ordering_rules:
                after_numbers = page_ordering_rules[page_number]
                for after_number in after_numbers:
                    if after_number in remaining_pages:
                        valid_page = False
                        break

        if valid_page:
            valid_page_updates.append(page_update)
        else:
            invalid_page_updates.append(page_update)

    return valid_page_updates, invalid_page_updates


def get_middle_page_number_total(page_information: list[str]) -> int:
    page_ordering_rules, page_updates = _get_page_ordering_rules_page_updates(page_information)
    valid_page_updates, invalid_page_updates = _get_valid_invalid_page_updates(page_ordering_rules, page_updates)

    middle_pages: list[int] = []
    for page_update in valid_page_updates:
        middle_page = page_update[len(page_update) // 2]
        middle_pages.append(middle_page)

    return sum(middle_pages)


def _correct_invalid_page_updates(page_ordering_rules: dict[int, list[int]], invalid_page_updates: list[list[int]]):
    for invalid_page_update in invalid_page_updates:
        for page_index, page_number in enumerate(invalid_page_update):
            remaining_pages = invalid_page_update[page_index + 1:]
            if page_number in page_ordering_rules:
                after_numbers = page_ordering_rules[page_number]
                for after_number in after_numbers:
                    if after_number in remaining_pages:
                        other_number_index = invalid_page_update.index(after_number)
                        # Swap the two numbers
                        invalid_page_update[page_index], invalid_page_update[other_number_index] = (
                            invalid_page_update[other_number_index],
                            invalid_page_update[page_index]
                        )


def get_corrected_middle_page_number_total(page_information: list[str]) -> int:
    page_ordering_rules, page_updates = _get_page_ordering_rules_page_updates(page_information)
    valid_page_updates, invalid_page_updates = _get_valid_invalid_page_updates(page_ordering_rules, page_updates)

    corrected_invalid_page_updates: list[list[int]] = []
    while invalid_page_updates:
        _correct_invalid_page_updates(page_ordering_rules, invalid_page_updates)
        valid_page_updates, invalid_page_updates = _get_valid_invalid_page_updates(page_ordering_rules,
                                                                                   invalid_page_updates)
        corrected_invalid_page_updates.extend(valid_page_updates)

    middle_pages: list[int] = []
    for page_update in corrected_invalid_page_updates:
        middle_page = page_update[len(page_update) // 2]
        middle_pages.append(middle_page)

    return sum(middle_pages)
