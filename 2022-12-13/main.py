from ast import literal_eval
from functools import reduce, cmp_to_key


def compare(left: int | list[int], right: int | list[int]) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        for result in map(compare, left, right):
            if result:
                return result
        return compare(len(left), len(right))
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        return compare(left, [right])


if __name__ == "__main__":
    with open("input.txt") as f:
        packet_pairs = [
            (literal_eval(pair_lines.split()[0]), literal_eval(pair_lines.split()[1]))
            for pair_lines in f.read().split("\n\n")
        ]

    # Part 1
    result = sum(
        i
        for i, (left, right) in enumerate(packet_pairs, start=1)
        if compare(left, right) == 1
    )
    print(result)

    # Part 2
    sorted_packets = sorted(
        [*(reduce(lambda x, y: [*x, *y], packet_pairs)), [[2]], [[6]]],
        key=cmp_to_key(compare),
    )
    decoder_key = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
    print(decoder_key)
