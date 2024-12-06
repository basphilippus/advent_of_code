XMAS = "XMAS"


def _build_xmas_grid(word_search: list[str]) -> tuple[list[list[str]], list[list[str]]]:
    xmas_grid: list[list[str]] = []
    visualisation_grid: list[list[str]] = []
    for row in word_search:
        xmas_grid.append(list(row))
        visualisation_grid.append(["."] * len(row))

    return xmas_grid, visualisation_grid


def _traverse_grid(grid: list[list[str]],
                   visualisation_grid: list[list[str]],
                   origin: tuple[int, int],
                   direction: tuple[int, int]) -> int:
    current_index = 0
    current_position: tuple[int, int] = origin

    while current_index < len(XMAS):
        next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        if next_position[0] < 0 or next_position[0] >= len(grid) or next_position[1] < 0 or next_position[1] >= len(grid[0]):
            return 0

        next_character = grid[next_position[0]][next_position[1]]
        if next_character != XMAS[current_index + 1]:
            return 0

        if current_index + 1 == len(XMAS) - 1:
            break

        current_index += 1
        current_position = next_position

    # Fill in the visualisation grid
    for i in range(len(XMAS)):
        visualisation_grid[origin[0] + i * direction[0]][origin[1] + i * direction[1]] = XMAS[i]

    return 1


def get_amount_of_xmas_occurrences(word_search: list[str]) -> int:
    xmas_grid, visualisation_grid = _build_xmas_grid(word_search)
    origin_points: list[tuple[int, int]] = []

    for row_index, row in enumerate(xmas_grid):
        for column_index, column in enumerate(row):
            if column == "X":
                origin_points.append((row_index, column_index))

    amount_of_xmas_occurrences = 0
    for origin_point in origin_points:
        # Right
        amount_of_xmas_occurrences += _traverse_grid(xmas_grid, visualisation_grid, origin_point, (0, 1))
        # Bottom Right
        amount_of_xmas_occurrences += _traverse_grid(xmas_grid, visualisation_grid, origin_point, (1, 1))
        # Bottom
        amount_of_xmas_occurrences += _traverse_grid(xmas_grid, visualisation_grid, origin_point, (1, 0))
        # Bottom Left
        amount_of_xmas_occurrences += _traverse_grid(xmas_grid, visualisation_grid, origin_point, (1, -1))
        # Left
        amount_of_xmas_occurrences += _traverse_grid(xmas_grid, visualisation_grid, origin_point, (0, -1))
        # Top Left
        amount_of_xmas_occurrences += _traverse_grid(xmas_grid, visualisation_grid, origin_point, (-1, -1))
        # Top
        amount_of_xmas_occurrences += _traverse_grid(xmas_grid, visualisation_grid, origin_point, (-1, 0))
        # Top Right
        amount_of_xmas_occurrences += _traverse_grid(xmas_grid, visualisation_grid, origin_point, (-1, 1))

    print()
    print("\n".join(["".join(row) for row in visualisation_grid]))
    print()

    return amount_of_xmas_occurrences


valid_xmas_shapes = [
    # M.S
    # .A.
    # M.S
    ["M", "S", "S", "M"],
    # M.M
    # .A.
    # S.S
    ["M", "M", "S", "S"],
    # S.M
    # .A.
    # S.M
    ["S", "M", "M", "S"],
    # S.S
    # .A.
    # M.M
    ["S", "S", "M", "M"],
]


def get_amount_of_xmas_shapes(word_search: list[str]) -> int:
    xmas_grid, visualisation_grid = _build_xmas_grid(word_search)
    origin_points: list[tuple[int, int]] = []

    for row_index, row in enumerate(xmas_grid):
        for column_index, column in enumerate(row):
            if column == "A":
                origin_points.append((row_index, column_index))

    amount_of_xmas_shapes = 0
    for origin_point in origin_points:
        if origin_point[0] == 0 or origin_point[0] == len(xmas_grid) - 1 or origin_point[1] == 0 or origin_point[1] == len(xmas_grid[0]) - 1:
            continue

        top_left = xmas_grid[origin_point[0] - 1][origin_point[1] - 1]
        top_right = xmas_grid[origin_point[0] - 1][origin_point[1] + 1]
        bottom_right = xmas_grid[origin_point[0] + 1][origin_point[1] + 1]
        bottom_left = xmas_grid[origin_point[0] + 1][origin_point[1] - 1]

        surrounding_characters = [top_left, top_right, bottom_right, bottom_left]
        if surrounding_characters in valid_xmas_shapes:

            # Fill in the visualisation grid
            visualisation_grid[origin_point[0]][origin_point[1]] = "A"
            visualisation_grid[origin_point[0] - 1][origin_point[1] - 1] = xmas_grid[origin_point[0] - 1][origin_point[1] - 1]
            visualisation_grid[origin_point[0] - 1][origin_point[1] + 1] = xmas_grid[origin_point[0] - 1][origin_point[1] + 1]
            visualisation_grid[origin_point[0] + 1][origin_point[1] - 1] = xmas_grid[origin_point[0] + 1][origin_point[1] - 1]
            visualisation_grid[origin_point[0] + 1][origin_point[1] + 1] = xmas_grid[origin_point[0] + 1][origin_point[1] + 1]

            amount_of_xmas_shapes += 1

    print()
    print("\n".join(["".join(row) for row in visualisation_grid]))
    print()

    return amount_of_xmas_shapes
