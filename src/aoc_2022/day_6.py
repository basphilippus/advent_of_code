from typing import List


def get_markers(datastream_buffer_inputs: List[str], marker_size: int) -> List[int]:
    start_of_packet_markers: List[int] = []
    for datastream_buffer_input in datastream_buffer_inputs:
        start_of_packet_marker = 0
        while start_of_packet_marker < len(datastream_buffer_input):
            if len(set(datastream_buffer_input[0 + start_of_packet_marker:marker_size + start_of_packet_marker])) \
                    == marker_size:
                start_of_packet_markers.append(start_of_packet_marker + marker_size)
                break
            start_of_packet_marker += 1

    return start_of_packet_markers
