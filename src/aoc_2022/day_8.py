from collections import defaultdict
from functools import reduce
from typing import List, Dict, Tuple


DEBUG = False


def get_amount_of_visible_trees(tree_height_input: List[str]) -> int:
    max_y, max_x, trees = build_tree_height_map(tree_height_input)

    print()
    visualize_height(trees)

    tree_visibility: Dict[int, List[bool]] = defaultdict(list)
    for y in range(max_y):
        for x in range(max_x):
            visibility = is_visible(y, x, max_y, max_x, trees)
            tree_visibility[y].insert(x, visibility)

    print()
    visualize_visibility(tree_visibility)

    total_visible_trees: List[bool] = reduce(lambda total_trees, tree_line:
                                             total_trees + tree_line, tree_visibility.values(), [])
    return sum(total_visible_trees)


def get_best_scenic_score(tree_height_input: List[str]) -> int:
    max_y, max_x, trees = build_tree_height_map(tree_height_input)

    print()
    visualize_height(trees)

    tree_scenic_scores: Dict[int, List[int]] = defaultdict(list)
    for y in range(max_y):
        for x in range(max_x):
            scenic_score = calculate_scenic_score(y, x, max_y, max_x, trees)
            tree_scenic_scores[y].insert(x, scenic_score)

    print()
    visualize_height(tree_scenic_scores)

    all_scenic_scores: List[int] = reduce(lambda total_trees, tree_line:
                                          total_trees + tree_line, tree_scenic_scores.values(), [])
    return max(all_scenic_scores)


def build_tree_height_map(tree_height_input: List[str]) -> Tuple[int, int, Dict[int, List[int]]]:
    trees: Dict[int, List[int]] = defaultdict(list)
    max_y, max_x = 0, 0
    for y, tree_height_line in enumerate(tree_height_input):
        for x, tree_height in enumerate(tree_height_line):
            trees[y].insert(x, int(tree_height))
            max_x = max(max_x, x + 1)
        max_y = max(max_y, y + 1)
    return max_y, max_x, trees


def is_visible(y: int, x: int, max_y: int, max_x: int, trees: Dict[int, List[int]]) -> bool:
    if y == 0 or x == 0 or y == max_y - 1 or x == max_x - 1:
        # edges are always visible
        return True

    height: int = trees[y][x]
    # check_top
    top_visible: bool = True
    for y_check in range(y - 1, -1, -1):
        if trees[y_check][x] >= height:
            top_visible = False
            break

    # check_bottom
    bottom_visible: bool = True
    for y_check in range(y + 1, max_y):
        if trees[y_check][x] >= height:
            bottom_visible = False
            break

    # check_left
    left_visible: bool = True
    for x_check in range(x - 1, -1, -1):
        if trees[y][x_check] >= height:
            left_visible = False
            break

    # check_right
    right_visible: bool = True
    for x_check in range(x + 1, max_x):
        if trees[y][x_check] >= height:
            right_visible = False
            break

    return top_visible or bottom_visible or left_visible or right_visible


def calculate_scenic_score(y: int, x: int, max_y: int, max_x: int, trees: Dict[int, List[int]]) -> int:
    height: int = trees[y][x]
    # check_top
    top_score: int = 0
    for y_check in range(y - 1, -1, -1):
        top_score += 1
        if trees[y_check][x] >= height:
            break

    # check_bottom
    bottom_score: int = 0
    for y_check in range(y + 1, max_y):
        bottom_score += 1
        if trees[y_check][x] >= height:
            break

    # check_left
    left_score: int = 0
    for x_check in range(x - 1, -1, -1):
        left_score += 1
        if trees[y][x_check] >= height:
            break

    # check_right
    right_score: int = 0
    for x_check in range(x + 1, max_x):
        right_score += 1
        if trees[y][x_check] >= height:
            break

    return top_score * bottom_score * left_score * right_score


def visualize_height(tree_height: Dict[int, List[int]]):
    if not DEBUG:
        return

    for _, height_line in tree_height.items():
        line = ''
        for height in height_line:
            line += f'{height}'.rjust(2, ' ')
        print(line)


def visualize_visibility(tree_visibility: Dict[int, List[bool]]):
    if not DEBUG:
        return

    for _, visibility_line in tree_visibility.items():
        line = ''
        for visibility in visibility_line:
            if visibility:
                line += 'V'.rjust(2, ' ')
            else:
                line += '.'.rjust(2, ' ')
        print(line)
