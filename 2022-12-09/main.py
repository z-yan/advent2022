from collections import namedtuple
from dataclasses import dataclass

Motion = namedtuple("Motion", "direction step")


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def normalize(self) -> "Point":
        return Point(self.x // max(1, abs(self.x)), self.y // max(1, abs(self.y)))

    def move(self, direction: str) -> "Point":
        if direction == "R":
            delta_x, delta_y = 1, 0
        elif direction == "D":
            delta_x, delta_y = 0, -1
        elif direction == "L":
            delta_x, delta_y = -1, 0
        else:
            delta_x, delta_y = 0, 1

        return Point(self.x + delta_x, self.y + delta_y)

    def is_adjacent_to(self, other: "Point"):
        return max(abs(self.x - other.x), abs(self.y - other.y)) <= 1


def simulate_rope(rope_length: int, motions: list[Motion]) -> int:
    rope = [Point(1, 1) for _ in range(rope_length)]
    visited = set()

    for motion in motions:
        for _ in range(motion.step):
            rope[0] = rope[0].move(motion.direction)

            for i in range(1, rope_length):
                curr_knot = rope[i]
                prev_knot = rope[i - 1]

                if not curr_knot.is_adjacent_to(prev_knot):
                    rope[i] += (prev_knot - curr_knot).normalize()

                if i == rope_length - 1:
                    visited.add(rope[i])

    return len(visited)


if __name__ == "__main__":
    motions = [
        Motion(line.split()[0], int(line.split()[1]))
        for line in open("input.txt").read().splitlines()
    ]

    # Part 1
    print(f"Part 1 visited: {simulate_rope(2, motions)}")

    # Part 2
    print(f"Part 2 visited: {simulate_rope(10, motions)}")
