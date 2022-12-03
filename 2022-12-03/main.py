import string

ITEM_PRIORITIES = {
    letter: i
    for i, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)
}

if __name__ == "__main__":
    with open("input.txt") as f:
        rucksacks = f.read().splitlines()

    # Part 1
    priority_sum = sum(
        ITEM_PRIORITIES[
            (
                set(rucksack[: len(rucksack) // 2])
                & set(rucksack[len(rucksack) // 2 :])
            ).pop()
        ]
        for rucksack in rucksacks
    )

    print(f"Priority sum: {priority_sum}")

    # Part 2
    badge_priority_sum = sum(
        ITEM_PRIORITIES[
            (set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])).pop()
        ]
        for i in range(0, len(rucksacks), 3)
    )

    print(f"Badge priority sum: {badge_priority_sum}")
