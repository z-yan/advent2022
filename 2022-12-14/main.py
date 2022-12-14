import numpy as np


# return new_pos, rest, stop
def unit_step(curr_pos, scan):
    options = [
        (curr_pos[0] + 1, curr_pos[1]),
        (curr_pos[0] + 1, curr_pos[1] - 1),
        (curr_pos[0] + 1, curr_pos[1] + 1),
    ]

    for new_pos in options:
        try:
            if scan[new_pos] == ".":
                curr_pos = new_pos
                return curr_pos, False, False
            if new_pos == options[-1]:
                scan[curr_pos] = "o"

                if curr_pos == (0, 500):
                    return curr_pos, True, True

                return curr_pos, True, False
        except IndexError:
            return curr_pos, False, True


def simulate(scan: np.ndarray) -> int:
    unit_count = 0
    start_pos = (0, 500)
    stop = False

    while not stop:
        curr_pos = start_pos
        rest = False

        while not (rest or stop):
            curr_pos, rest, stop = unit_step(curr_pos, scan)
            unit_count += rest

    return unit_count


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()

    scan = np.full((1000, 1000), fill_value=".")

    all_paths = list(
        [tuple(map(int, segment.split(",")[::-1])) for segment in line.split(" -> ")]
        for line in lines
    )

    for path in all_paths:
        for i in range(1, len(path)):
            a = path[i]
            b = path[i - 1]

            axis = 0 if a[0] != b[0] else 1

            if a[axis] > b[axis]:
                a, b = b, a

            scan[a[0] : b[0] + 1, a[1] : b[1] + 1] = "#"

    # Part 1
    print(simulate(scan.copy()))

    # Part 2
    scan[max(x[0] for path in all_paths for x in path) + 2 :] = "#"

    print(simulate(scan.copy()))
