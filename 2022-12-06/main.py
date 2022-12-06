def find_marker(input_string: str, marker_length: int = 4) -> int:
    for i in range(len(input_string)):
        if len(set(input_string[i : i + marker_length])) == marker_length:
            return i + marker_length

    # Message doesn't contain marker
    return -1


if __name__ == "__main__":
    with open("input.txt") as f:
        input_string = f.read()

    print(f"Start-of-packet marker at {find_marker(input_string)}")
    print(f"Start-of-message marker at {find_marker(input_string, 14)}")
