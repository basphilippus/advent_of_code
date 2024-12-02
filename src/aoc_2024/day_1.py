def calculate_total_distance(location_id_pairs: list[str]) -> int:
    left_list = []
    right_list = []

    for location_id_pair in location_id_pairs:
        left, right = location_id_pair.split('  ')
        left_list.append(int(left))
        right_list.append(int(right))

    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)

    total_distance = 0

    for i in range(len(sorted_left_list)):
        left_location_id = sorted_left_list[i]
        right_location_id = sorted_right_list[i]

        total_distance += abs(left_location_id - right_location_id)

    return total_distance


def calculate_similarity_score(location_id_pairs: list[str]) -> int:
    left_list = []
    right_list = []

    for location_id_pair in location_id_pairs:
        left, right = location_id_pair.split('  ')
        left_list.append(int(left))
        right_list.append(int(right))

    right_occurrence_map = {}
    for location_id in right_list:
        if location_id in right_occurrence_map:
            right_occurrence_map[location_id] += 1
        else:
            right_occurrence_map[location_id] = 1

    similarity_score = 0
    for location_id in left_list:
        occurrence = right_occurrence_map.get(location_id, 0)
        similarity_score += location_id * occurrence

    return similarity_score
