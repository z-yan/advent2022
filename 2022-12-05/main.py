import copy
import re


# item_count, source, destination
def parse_instruction_line(line: str) -> tuple[int, int, int]:
    return tuple(map(int, re.match(r"move (\d*) from (\d) to (\d)", line).groups()))


def stacks_to_output(stacks: dict[list[str]]) -> str:
    output_string = str()

    for key in sorted(stacks.keys()):
        output_string += stacks[key][-1]

    return output_string


if __name__ == "__main__":
    with open("input.txt") as f:
        input_string = f.read()
        initial_state, instructions = input_string.split("\n\n")

    # initialize stacks
    initial_state_lines = initial_state.split("\n")
    stacks = {
        int(stack_number): list() for stack_number in initial_state_lines.pop().split()
    }

    for initial_state_line in reversed(initial_state_lines):
        for i in range(1, len(stacks) + 1):
            next_item = initial_state_line[
                4 * i - 3
            ]  # index derived from number of previous characters

            if next_item.isalpha():
                stacks[i].append(next_item)

    stacks_initial = copy.deepcopy(stacks)

    # process instructions
    instructions = [
        parse_instruction_line(instruction_line)
        for instruction_line in instructions.splitlines()
    ]

    # Part 1
    for item_count, source, destination in instructions:
        # Move one item at a time
        for _ in range(item_count):
            item = stacks[source].pop()
            stacks[destination].append(item)

    print(f"End arrangement: {stacks_to_output(stacks)}")

    # Part 2
    # CrateMover 9001
    stacks = stacks_initial

    # Move whole sublists
    for item_count, source, destination in instructions:
        to_be_moved, stacks[source] = (
            stacks[source][-item_count:],
            stacks[source][:-item_count],
        )
        stacks[destination] += to_be_moved

    print(f"End arrangement: {stacks_to_output(stacks)}")
