if __name__ == "__main__":
    with open("input.txt") as f:
        input_lines = f.read().splitlines()

    pairs = [
        (
            tuple(map(int, line.split(",")[0].split(sep="-"))),
            tuple(map(int, line.split(",")[1].split(sep="-"))),
        )
        for line in input_lines
    ]

    # Part 1
    subset_count = sum(
        (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1])
        or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1])
        for pair in pairs
    )

    print(f"Subset count: {subset_count}")

    # Part 2
    overlaps_count = sum(
        bool(
            set(range(pair[0][0], pair[0][1] + 1))
            & set(range(pair[1][0], pair[1][1] + 1))
        )
        for pair in pairs
    )

    print(f"Overlaps count: {overlaps_count}")
